from rest_framework import generics

from books.models import Book
from books.serializers import BookSerializer


class GetBooksView(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
