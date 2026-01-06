from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import Token
from django.utils.translation import gettext as _
from apps.users.models import CustomUser
from django.db.models import Q


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token: Token):
        print(validated_token.payload)
        try:
            user_data = validated_token['user_data']
        except KeyError:
            raise InvalidToken(
                _("Token contained no recognizable user identification")
            ) 
        # user = CustomUser.objects.get(
        #     Q(id=user_data['id'])
        #     | 
        #     Q(username=user_data['username'])
        #     | 
        #     Q(email=user_data['email']))
        # user = self.CustomUser.objects.get(email=user_data['email'] or username=user_data['username'])    
        user = CustomUser(**user_data)
        if api_settings.CHECK_USER_IS_ACTIVE and not user.is_active:
            raise AuthenticationFailed(_("User is inactive"), code="user_inactive")
        
        return user