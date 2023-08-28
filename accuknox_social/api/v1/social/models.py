import uuid

from django.contrib.auth import get_user_model
from django.db import models

from .utils.constants import FriendRequestStatus

User = get_user_model()

class Friends(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='main_user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_of')

    def __str__(self):
        return f"Friends of {self.user}"

class FriendRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_requests_sent')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_requests_received')
    status = models.CharField(max_length=20, choices=[(status.value, status.name) for status in FriendRequestStatus], default=FriendRequestStatus.PENDING.value)
    def __str__(self):
        return f"{self.requester} -> {self.recipient} ({self.status})"
