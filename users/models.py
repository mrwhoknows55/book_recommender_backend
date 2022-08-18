from django.contrib.auth.models import AbstractUser
from django.db import models

from books.models import Book


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    library = models.ManyToManyField(Book, related_name="user")
    recommendations = models.ManyToManyField(Book, related_name="recommended_user")
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [name, email, password]
