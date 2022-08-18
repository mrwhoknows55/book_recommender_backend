from recommendation.views import GetRecommendationsView
from django.urls import path

urlpatterns = [
    path('recom/', GetRecommendationsView.as_view())
]
