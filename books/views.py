from django.shortcuts import render, get_object_or_404

from books.models import Author, Book


def index(request):
    all_books = Book.objects.all()
    context = {'all_books': all_books,}
    return render(request, 'books/index.html', context)


def author_detail(request, a_id):
    author = Author.objects.all().filter(id=a_id)[0]
    context = {'author': author, }
    return render(request, 'books/author_details.html', context)


def book_detail(request, b_id):
    book = get_object_or_404(Book, id=b_id)
    context = {'book': book, }
    return render(request, 'books/book_detail.html', context)
