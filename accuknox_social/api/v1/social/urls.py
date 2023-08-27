from django.urls import path
from .views import FriendRequestView, AcceptRejectFriendRequestView, ListFriendsView

urlpatterns = [
    path('add_friend/<str:recipient_id>', FriendRequestView.as_view(), name='send-friend-request'),
    path('response/<str:friend_request_id>', AcceptRejectFriendRequestView.as_view(), name='accept-reject-friend-request'),
    path('friends', ListFriendsView.as_view(), name='list-friends')
]