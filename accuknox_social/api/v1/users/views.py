from django.contrib.auth import authenticate, get_user_model, login
from django.db import models
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from ...utils import CustomPageNumberPagination
from .serializers import CustomLoginSerializer, SignupSerializer

User = get_user_model()

class SignupAPIView(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny,]

class LoginAPIView(ObtainAuthToken):
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            email = serializer.validated_data['email'].lower()
            password = serializer.validated_data['password']
            user = authenticate(request=request, email=email, password=password)

            if user:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({'token': token.key})
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def post(self, request):
        request.auth.delete()
        return JsonResponse({'detail': 'Logout successful'}, status=status.HTTP_200_OK)

class UserListAPIView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        user = self.request.user
        search_keyword = self.request.query_params.get('search', '').strip()
        users = User.objects.exclude(id=user.id)
        if search_keyword:
            users = User.objects.filter(
            models.Q(email__iexact=search_keyword) | models.Q(first_name__icontains=search_keyword) | models.Q(last_name__icontains=search_keyword)
        )
        return users

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        response_data = [
            {'email': query.email, 'name': f'{query.first_name} {query.last_name}'}
            for query in queryset
        ]

        page = self.paginate_queryset(response_data)
        if page is not None:
            return self.get_paginated_response(page)
