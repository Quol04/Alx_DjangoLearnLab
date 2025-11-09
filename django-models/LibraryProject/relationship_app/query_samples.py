
from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author.
def books_by_author(author_id):
    author = Author.objects.get(id=author_id)  # Replace with the desired author ID or pass dynamically
    return author.books.all()


def books_by_author_name(author_name):
    """Find an Author by name and return books written by that author using a filter query.

    This function intentionally uses the form `Author.objects.get(name=author_name)` and
    `Book.objects.filter(author=author)` to demonstrate both lookup styles.
    """
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


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


def get_librarian_by_lookup(library_id=None, library_name=None):
    """Retrieve a Librarian object using an explicit lookup on the Librarian model.

    This demonstrates `Librarian.objects.get(library=...)` as requested.
    """
    if library_id is not None:
        library = Library.objects.get(id=library_id)
    elif library_name is not None:
        library = Library.objects.get(name=library_name)
    else:
        raise ValueError('Either library_id or library_name must be provided')

    # explicit lookup on the Librarian model by its related library
    return Librarian.objects.get(library=library)


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

        # Demonstrate explicit Librarian.objects.get(library=...)
        try:
            lib_by_lookup = get_librarian_by_lookup(library_id=library_id)
            print(f"\n(Lookup) Librarian for Library (id={library_id}): {lib_by_lookup.name}")
        except Exception as e:
            print(f"\n(Lookup) Could not find librarian via Librarian.objects.get: {e}")

    except Exception as e:
        print(f"Error running sample queries: {e}")