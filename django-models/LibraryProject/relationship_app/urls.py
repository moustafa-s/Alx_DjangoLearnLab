from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import user_login
from .views import user_logout
from .views import register

urlpatterns = [
    path("books/", list_books, name="list_books"),  # URL for function-based view
    path(
        "library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"
    ),  # URL for class-based view
    path("login/", user_login, name="login"),  # URL for login page
    path("logout/", user_logout, name="logout"),  # URL for logout page
    path("register/", register, name="register"),  # URL for registration page
]
