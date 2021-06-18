from django.urls import path
from .views import GetBooksMetaView, GetBookDetailView

urlpatterns = [
    path('books', GetBooksMetaView.as_view()),
    path('books/<int:pk>/', GetBookDetailView.as_view())
]
