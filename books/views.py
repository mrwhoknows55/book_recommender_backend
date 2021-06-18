from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from books.serializers import BookMetaInfoSerializer, BookDetailsSerializer


class GetBooksMetaView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookMetaInfoSerializer


class GetBookDetailView(APIView):
    def get(self, request, pk):
        book_details = Book.objects.get(book_id=pk)
        serializer = BookDetailsSerializer(book_details)
        return Response(serializer.data)
