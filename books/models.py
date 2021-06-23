from django.db import models


class Book(models.Model):
    book_id = models.BigAutoField(null=False, primary_key=True)
    goodreads_book_id = models.BigIntegerField()
    best_book_id = models.BigIntegerField()
    work_id = models.BigIntegerField()
    books_count = models.IntegerField()
    isbn = models.BigIntegerField(null=False)
    isbn13 = models.BigIntegerField()
    authors = models.TextField(max_length=510)
    original_publication_year = models.IntegerField()
    original_title = models.TextField()
    title = models.TextField(null=False)
    language_code = models.CharField(max_length=10)
    ratings_count = models.IntegerField()
    work_ratings_count = models.IntegerField()
    work_text_reviews_count = models.IntegerField()
    ratings_1 = models.IntegerField()
    ratings_2 = models.IntegerField()
    ratings_3 = models.IntegerField()
    ratings_4 = models.IntegerField()
    ratings_5 = models.IntegerField()
    image_url = models.TextField()
    small_image_url = models.TextField()
    avg_rating = models.FloatField()

    class Meta:
        managed = False
        db_table = 'books_book_view'
