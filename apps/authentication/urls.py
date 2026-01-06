from django.urls import path
from apps.authentication.views.authentication_views import CustomRetriveUpdateAPIView, LogoutAPIView
# from rest_framework_simplejwt.views import TokenObtainPairView
from apps.authentication.views.authentication_views import UserLoginAPIView


urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    # path('login//', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', CustomRetriveUpdateAPIView.as_view(), name='profile'),
    path('profile/logout/', LogoutAPIView.as_view(), name='logout'),
]
