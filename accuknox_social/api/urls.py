from django.urls import path, include

urlpatterns = [
    path('v1/users/', include('api.v1.users.urls'))
]