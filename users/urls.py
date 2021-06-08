from django.urls import path
from .views import SignUpView, LoginView, UserView, LogoutView

urlpatterns = [
    path('signup', SignUpView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view())
]
