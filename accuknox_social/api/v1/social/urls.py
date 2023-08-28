from django.urls import path

from .views import (AcceptRejectFriendRequestView, FriendRequestView,
                    ListFriendsView, PendingFriendRequestListView)

urlpatterns = [
    path('add_friend/<str:recipient_id>', FriendRequestView.as_view(), name='send-friend-request'),
    path('response/<str:friend_request_id>', AcceptRejectFriendRequestView.as_view(), name='accept-reject-friend-request'),
    path('friends', ListFriendsView.as_view(), name='list-friends'),
    path('pending-friend-requests', PendingFriendRequestListView.as_view(), name='pending-friend-requests')
]
