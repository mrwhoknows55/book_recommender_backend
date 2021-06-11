from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from books.serializers import BookSerializer
from rest_framework import generics


class GetBooksView(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
