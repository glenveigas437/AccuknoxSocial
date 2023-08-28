from django.urls import include, path

from .views import LoginAPIView, LogoutAPIView, SignupAPIView, UserListAPIView

urlpatterns = [
    path('signup', SignupAPIView.as_view(), name='signup'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
    path('all', UserListAPIView.as_view(), name='all-users')
]
