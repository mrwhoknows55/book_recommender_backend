from django.urls import path

from .views import SignUpView, LoginView, UserView, LogoutView, PostLibraryView, GetLibraryView, GetWishlistView, PostWishlistView

urlpatterns = [
    path('signup', SignUpView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('library/', GetLibraryView.as_view()),
    path('library/<int:pk>', PostLibraryView.as_view()),
    path('library/<int:pk>/', PostLibraryView.as_view()),
    path('wishlist/', GetWishlistView.as_view()),
    path('wishlist/<int:pk>', PostWishlistView.as_view()),
    path('wishlist/<int:pk>/', PostWishlistView.as_view())
]
