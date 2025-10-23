from rest_framework import serializers

from apps.books.models.book_models import Book


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'