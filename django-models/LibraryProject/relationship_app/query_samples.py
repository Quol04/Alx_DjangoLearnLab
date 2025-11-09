# Prepare a Python script query_samples.py in the relationship_app directory. This script should contain the query for each of the following of relationship:
# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
author = Author.objects.get(id=1)  # Replace with the desired author ID
books_by_author = author.books.all()

# List all books in a library.
library = Library.objects.get(name = Library.name)  # Replace with the desired library ID
books_in_library = library.books.all()

# Retrieve the librarian for a library.
librarian = library.librarian
print(f"Books by Author {author.name}:")
for book in books_by_author:
    print(f"- {book.title}")

print(f"Books in Library {library.name}:")
for book in books_in_library:
    print(f"- {book.title}")

print(f"Librarian for Library {library.name}: {librarian.name}")