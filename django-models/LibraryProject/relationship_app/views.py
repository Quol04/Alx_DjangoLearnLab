from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group


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


# --- Role checks and role-protected views ---
def is_admin(user):
    """Return True for site staff or superusers."""
    return bool(user and user.is_authenticated and (user.is_staff or user.is_superuser))


def is_librarian(user):
    """Return True if the user is a librarian.

    This checks for a group named 'Librarian' or an attribute `is_librarian` on the user.
    Adjust to your project's auth model (custom user fields or groups) as needed.
    """
    if not (user and user.is_authenticated):
        return False
    if user.is_superuser:
        return True
    if getattr(user, 'is_librarian', False):
        return True
    return user.groups.filter(name='Librarian').exists()


def is_member(user):
    """Return True if the user is a library member.

    Checks group 'Member' or attribute `is_member` on the user.
    """
    if not (user and user.is_authenticated):
        return False
    if getattr(user, 'is_member', False):
        return True
    return user.groups.filter(name='Member').exists()


@user_passes_test(is_admin, login_url='login')
def admin_view(request):
    """View accessible only to admins/staff."""
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian, login_url='login')
def librarian_view(request):
    """View accessible only to librarians."""
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member, login_url='login')
def member_view(request):
    """View accessible only to library members."""
    return render(request, 'relationship_app/member_view.html')

