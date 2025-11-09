from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.
# Implement Function-based View:

# Create a function-based view in relationship_app/views.py that lists all books stored in the database.
# This view should render a simple text list of book titles and their authors.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})




class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# Authentication views
def register(request):
    """Register a new user using Django's built-in UserCreationForm.

    On successful registration the new user is automatically logged in
    and redirected to the site root ('/'). Adjust the redirect target
    as needed for your project (for example, to a dashboard or home page).
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})


class AppLoginView(LoginView):
    """Wrapper around Django's built-in LoginView.

    Provide `template_name` pointing to `relationship_app/login.html`.
    You can set `next` or `redirect_authenticated_user` in URLs as needed.
    """
    template_name = 'relationship_app/login.html'


class AppLogoutView(LogoutView):
    """Wrapper around Django's built-in LogoutView.

    After logout this view will display `relationship_app/logged_out.html`.
    """
    template_name = 'relationship_app/logged_out.html'

# Note: Role-based views (admin_view, librarian_view, member_view) are
# implemented in their respective files as per the project structure.

    