from django.urls import path
from apps.authentication.views.authentication_views import LoginAPIView, CustomRetriveUpdateAPIView, LogoutAPIView


urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', CustomRetriveUpdateAPIView.as_view(), name='profile'),
    path('profile/logout/', LogoutAPIView.as_view(), name='logout'),
]
