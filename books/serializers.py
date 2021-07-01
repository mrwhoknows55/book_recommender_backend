from rest_framework import serializers
from .models import Book


class BookMetaInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id', 'isbn', 'title', 'authors', "genre", 'image_url', 'avg_rating', 'ratings_count']


class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "book_id",
            "isbn",
            "isbn13",
            "title",
            "original_title",
            "authors",
            "image_url",
            "genre",
            "original_publication_year",
            "description",
            "avg_rating",
            "ratings_count",
            "work_ratings_count"
        ]
