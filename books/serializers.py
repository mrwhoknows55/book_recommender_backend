from rest_framework import serializers
from .models import Book


class BookMetaInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id', 'isbn', 'title', 'authors', 'image_url', 'avg_rating', 'ratings_count']


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
            "language_code",
            "original_publication_year",
            "image_url",
            "books_count",
            "ratings_count",
            "work_ratings_count",
            "work_text_reviews_count",
            "goodreads_book_id",
            "best_book_id",
            "work_id",
            "ratings_1",
            "ratings_2",
            "ratings_3",
            "ratings_4",
            "ratings_5",
            "avg_rating"
        ]
