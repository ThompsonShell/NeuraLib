from django.urls import path
from apps.users.views import UserListCreateAPIView


urlpatterns = [
    path('users', UserListCreateAPIView.as_view(), name='user-list-create'),
]