from django.urls import path
from .views import GetBooksView

urlpatterns = [
    path('books', GetBooksView.as_view())
]
