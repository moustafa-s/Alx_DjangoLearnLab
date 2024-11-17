from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("books/", list_books, name="list_books"),  # URL for function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    # URL for class-based view
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),  # Login view
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),  # Logout view
    path("register/", views.register, name="register"),  # Registration view (custom)
]
