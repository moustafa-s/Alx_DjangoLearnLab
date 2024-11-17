from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),  # URL for function-based view
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
    path("admin/", views.admin_view, name="admin_view"),
    path("librarian/", views.librarian_view, name="librarian_view"),
    path("member/", views.member_view, name="member_view"),
    path("add/", views.add_book, name="add_book"),
    path("edit/<int:book_id>/", views.edit_book, name="edit_book"),
    path("delete/<int:book_id>/", views.delete_book, name="delete_book"),
]
