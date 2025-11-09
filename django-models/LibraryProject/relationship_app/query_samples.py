# Prepare a Python script query_samples.py in the relationship_app directory. This script should contain the query for each of the following of relationship:
# Query all books by a specific author.

# List all books in a library.
# Retrieve the librarian for a library.
from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author.
def books_by_author(author_id):
    author = Author.objects.get(id=author_id)  # Replace with the desired author ID or pass dynamically
    return author.books.all()


# List all books in a library (lookup by ID).
def books_in_library_by_id(library_id):
    library = Library.objects.get(id=library_id)
    return library.books.all()


# List all books in a library (lookup by name).
def books_in_library_by_name(library_name):
    """Retrieve a Library by name and return all related books.

    Example usage:
        books = books_in_library_by_name('Central Library')
    """
    library = Library.objects.get(name=library_name)
    return library.books.all()


# Retrieve the librarian for a library.
def get_librarian_for_library(library_id=None, library_name=None):
    if library_id is not None:
        library = Library.objects.get(id=library_id)
    elif library_name is not None:
        library = Library.objects.get(name=library_name)
    else:
        raise ValueError('Either library_id or library_name must be provided')

    return getattr(library, 'librarian', None)


if __name__ == '__main__':
    # Example CLI-style usage; adjust IDs/names as needed for your DB
    author_id = 1
    library_id = 1
    library_name = 'Central Library'  # Replace with the actual library name in your DB

    try:
        print(f"Books by Author (id={author_id}):")
        for book in books_by_author(author_id):
            print(f"- {book.title}")

        print(f"\nBooks in Library (id={library_id}):")
        for book in books_in_library_by_id(library_id):
            print(f"- {book.title}")

        print(f"\nBooks in Library (name='{library_name}'):")
        for book in books_in_library_by_name(library_name):
            print(f"- {book.title}")

        librarian = get_librarian_for_library(library_id=library_id)
        if librarian:
            print(f"\nLibrarian for Library (id={library_id}): {librarian.name}")
        else:
            print(f"\nNo librarian associated with Library (id={library_id})")

    except Exception as e:
        print(f"Error running sample queries: {e}")