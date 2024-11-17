from relationship_app.models import Author, Book


# Query 1: All books by a specific author
def get_books_by_author(author_name):
    try:
        # Retrieve the author object by name
        author = Author.objects.get(name=author_name)
        # Use filter to fetch all books by this author
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return []


# Query 2: List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []


# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None
