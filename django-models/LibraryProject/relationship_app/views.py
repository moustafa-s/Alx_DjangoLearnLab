from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .models import Library
from .models import UserProfile
from django.views.generic.detail import DetailView
from .forms import BookForm  # Assuming you have a form for Book

# Django’s Built-in Authentication Views and Forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

# Create your views here.


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Get all books
    return render(request, "relationship_app/list_books.html", {"books": books})


# View to add a new book (only accessible if the user has 'can_add_book' permission)
@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")  # Redirect to a page that lists all books
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})


# View to edit an existing book (only accessible if the user has 'can_change_book' permission)
@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")  # Redirect to a page that lists all books
    else:
        form = BookForm(instance=book)
    return render(
        request, "relationship_app/edit_book.html", {"form": form, "book": book}
    )


# View to delete a book (only accessible if the user has 'can_delete_book' permission)
@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")  # Redirect to a page that lists all books
    return render(request, "relationship_app/confirm_delete.html", {"book": book})


# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Template for displaying library details
    context_object_name = (
        "library"  # This will be the context variable passed to the template
    )


# Register View (For user registration)
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Create new user
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("login")  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # Redirect to home or dashboard
            else:
                messages.error(request, "Invalid credentials, please try again.")
        else:
            messages.error(request, "Invalid credentials, please try again.")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


# Logout View
def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


# Function to check if user is admin
def is_admin(user):
    return user.userprofile.role == "Admin"


# Function to check if user is a librarian
def is_librarian(user):
    return user.userprofile.role == "Librarian"


# Function to check if user is a member
def is_member(user):
    return user.userprofile.role == "Member"


# Admin view (only accessible by Admins)
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


# Librarian view (only accessible by Librarians)
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


# Member view (only accessible by Members)
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")
