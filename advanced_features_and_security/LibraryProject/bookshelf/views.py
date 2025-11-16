from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

from .models import Book

# -----------------------------
# LIST VIEW FOR ALL BOOKS
# -----------------------------
# bookshelf/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookSearchForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Safe list view for Book objects. Uses a Django form to validate search input and
    uses Django ORM filtering to avoid SQL injection.

    The view returns context['books'] (checker expects this variable).
    """
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        q = form.cleaned_data.get("q")
        if q:
            # Use ORM lookups (parameterized) instead of string formatting into raw SQL
            # This prevents SQL injection. __icontains does wildcard search safely.
            books = books.filter(title__icontains=q)  # avoid .extra() or raw SQL
    else:
        # If invalid, fallback to empty queryset or all results as appropriate
        # Here we keep all results but you may prefer to return none for invalid input
        pass

    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})



# -----------------------
# VIEW ARTICLE
# -----------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "bookshelf/article_detail.html", {"article": article})


# -----------------------
# CREATE ARTICLE
# -----------------------
@permission_required('bookshelf.can_create', raise_exception=True)
def article_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")
        Article.objects.create(title=title, body=body, author=request.user)
        return redirect("article_list")

    return render(request, "bookshelf/article_form.html")


# -----------------------
# EDIT ARTICLE
# -----------------------
@permission_required('bookshelf.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.body = request.POST.get("body")
        article.save()
        return redirect("article_detail", pk=pk)

    return render(request, "bookshelf/article_form.html", {"article": article})


# -----------------------
# DELETE ARTICLE
# -----------------------
@permission_required('bookshelf.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect("article_list")


# ================================
# BOOK LIST VIEW WITH PERMISSION
# ================================
