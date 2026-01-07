from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.users.models import CustomUser
from apps.authentication.serializers.user_serializer import UserSerializer
from apps.authentication.serializers.login_serializer import LoginSerializer


class LoginAPIView(APIView):
    def post(self, request):
        username, password = request.data.get('username'), request.data.get('password')
        if username and password:
            user = authenticate(request=request, username=username, password=password)
            if user is None:
                raise ValidationError("Invalid username or password.")
            token_obj, _ = Token.objects.get_or_create(user_id=user.pk)
            
        else:
            raise ValidationError("Username and password are required.")        
        return Response({"token": token_obj.key})
    
    
class CustomRetriveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
    
    
    
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        Token.objects.filter(user_id=user.pk).delete()
        return Response({"detail": "Successfully logged out."})    
    
    

class UserLoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer
    
    def perform_create(self, serializer):
        pass