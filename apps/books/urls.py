from django.urls import path
from apps.books.views import book_views

urlpatterns = [
    path('', book_views.BookCreateAPIView.as_view(), name='book-create')
]

