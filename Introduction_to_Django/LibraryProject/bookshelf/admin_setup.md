# Django Admin Setup for Book Model

## Registering the Book Model

In `bookshelf/admin.py`, import the `Book` model and register it with the Django admin interface to enable management functionality.

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
