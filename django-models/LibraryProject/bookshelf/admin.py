from django.contrib import admin
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication_year in the list view
    list_display = ("title", "author", "publication_year")

    # Add filters to filter books by publication year
    list_filter = ("publication_year",)

    # Add a search bar to search books by title or author
    search_fields = ("title", "author")


admin.site.register(Book, BookAdmin)
