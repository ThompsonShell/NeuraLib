from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from apps.users.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from apps.users.serializers.user_serializer import UserListCreateSerializer
from rest_framework.generics import ListCreateAPIView


# class UserListCreateView(ListCreateAPIView):
#     def get(self, request):
#         users = CustomUser.objects.all()
#         serializer = UserListCreateSerializer(users, many=True)
#         permission_classes = [IsAuthenticated]
#         return Response(serializer.data)


#     def post(self, request):
#         serializer = UserListCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListCreateAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserListCreateSerializer
    permission_classes = [IsAuthenticated]