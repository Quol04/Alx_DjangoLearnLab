from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output:
# The book instance is successfully created and stored in the database.
# Example: <Book: 1984 by George Orwell>
