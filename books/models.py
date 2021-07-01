from django.db import models


class Book(models.Model):
    book_id = models.BigAutoField(null=False, primary_key=True)
    isbn = models.TextField(max_length=20, null=False)
    isbn13 = models.BigIntegerField()
    title = models.TextField(null=False)
    original_title = models.TextField()
    authors = models.TextField(max_length=255)
    image_url = models.TextField()
    genre = models.TextField(default='')
    original_publication_year = models.IntegerField(max_length=4, default=0, db_column='publication_year')
    description = models.TextField(default='')
    avg_rating = models.FloatField()
    ratings_count = models.IntegerField()
    work_ratings_count = models.IntegerField()
