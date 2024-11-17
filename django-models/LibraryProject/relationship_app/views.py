from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Django’s Built-in Authentication Views and Forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required , user_passes_test
from django.contrib import messages
from .models import UserProfile
# Create your views here.


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Get all books
    return render(request, "relationship_app/list_books.html", {"books": books})


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
    return user.userprofile.role == 'Admin'

# Function to check if user is a librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Function to check if user is a member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view (only accessible by Admins)
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view (only accessible by Librarians)
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view (only accessible by Members)
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')