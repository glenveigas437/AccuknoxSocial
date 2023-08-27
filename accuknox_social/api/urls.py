from django.urls import path, include

urlpatterns = [
    path('v1/users/', include('api.v1.users.urls')),
    path('v1/social/', include('api.v1.social.urls'))
]