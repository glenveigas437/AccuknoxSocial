from rest_framework import generics, status
from .models import FriendRequest
from .serializers import FriendRequestSerializer
from django_ratelimit.decorators import ratelimit
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from django.db import models
from django.http import JsonResponse
from django.utils.decorators import method_decorator

User = get_user_model()

@method_decorator(ratelimit(key='user', rate='3/m', block=True), name='dispatch')
class FriendRequestView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def perform_create(self, serializer):
        requester = self.request.user
        recipient_id = self.kwargs['recipient_id']

        try:
            recipient = User.objects.get(pk=recipient_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Recipient not found.'}, status=status.HTTP_404_NOT_FOUND, content_type='application/json')
        
        existing_request = FriendRequest.objects.filter(
            (models.Q(requester=requester, recipient=recipient) | models.Q(requester=recipient, recipient=requester)),
            status__in=['pending', 'accepted']
        ).first()

        if existing_request:
            return JsonResponse({'error': 'Friend request already exists.'}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
        
        serializer.save(requester=requester, recipient=recipient)

        success_response = f'Sent Friend Request to {recipient.first_name} {recipient.last_name}'
        return JsonResponse({'message': success_response}, status=status.HTTP_201_CREATED, content_type='application/json')

class AcceptRejectFriendRequestView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, friend_request_id, *args, **kwargs):
        action = request.query_params.get('action', '').lower()

        try:
            friend_request = FriendRequest.objects.get(id=friend_request_id)
        except FriendRequest.DoesNotExist:
            return Response({'error': 'Friend request not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the request recipient is the current user
        if friend_request.recipient != request.user:
            return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

        if action == 'accept':
            # Check if the friend request is pending
            if friend_request.status != 'pending':
                return Response({'error': 'This friend request cannot be accepted.'}, status=status.HTTP_400_BAD_REQUEST)

            # Update the friend request status to "accepted"
            friend_request.status = 'accepted'
            friend_request.save()

            return Response({'message': 'Friend request accepted.'}, status=status.HTTP_200_OK)
        elif action == 'reject':
            # Check if the friend request is pending
            if friend_request.status != 'pending':
                return Response({'error': 'This friend request cannot be rejected.'}, status=status.HTTP_400_BAD_REQUEST)

            # Update the friend request status to "rejected"
            friend_request.status = 'rejected'
            friend_request.save()

            return Response({'message': 'Friend request rejected.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid action parameter.'}, status=status.HTTP_400_BAD_REQUEST)
