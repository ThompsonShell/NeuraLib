from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import timedelta

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)
    
    def validate(self, attrs):
        user = authenticate(
            request=self.context.get('request'),
            username=attrs.get('username'),
            email=attrs.get('email'),
            password=attrs.get('password')
        )
        if user is None:
            raise serializers.ValidationError("Invalid credentials provided.")
        referesh_token = RefreshToken.for_user(user)
        # referesh_token.payload['username'] = user.username
        # referesh_token.payload['email'] = user.email     
        referesh_token.payload['user_data'] = {
            'id': str(user.id),
            'username': user.username,
            'email': user.email,
            'is_active': user.is_active
        } 
        access_token = referesh_token.access_token
        access_token.set_exp(from_time=timezone.now(), lifetime=timedelta(hours=2))
        attrs['access'] = str(referesh_token.access_token)
        return attrs