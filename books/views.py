from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from books.serializers import BookMetaInfoSerializer, BookDetailsSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'limit'
    max_page_size = 30


class GetBooksMetaView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookMetaInfoSerializer
    pagination_class = StandardResultsSetPagination


class GetBookDetailView(APIView):
    def get(self, request, pk):
        book_details = Book.objects.get(book_id=pk)
        serializer = BookDetailsSerializer(book_details)
        return Response(serializer.data)
