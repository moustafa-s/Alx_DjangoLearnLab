# CRUD Operations for Book Model

## Create Operation
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
Expected Output: <Book: 1984 by George Orwell (1949)>


retrieved_book = Book.objects.get(id=book.id)
retrieved_book
Expected Output: <Book: 1984 by George Orwell (1949)>

retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
retrieved_book
Expected Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

retrieved_book.delete()
Book.objects.all()
Expected Output: <QuerySet []>