from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.books.serializers import BookCreateSerializer


class BookCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)


    def post(self, request):
        serializer = BookCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
