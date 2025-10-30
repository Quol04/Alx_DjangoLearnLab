from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title and save
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
print(book.title)

# Expected Output:
# Nineteen Eighty-Four
