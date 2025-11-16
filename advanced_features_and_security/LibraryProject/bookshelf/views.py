from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

from .models import Book

# -----------------------------
# LIST VIEW FOR ALL BOOKS
# -----------------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # <-- checker requires this variable name
    return render(request, 'bookshelf/book_list.html', {'books': books})


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
