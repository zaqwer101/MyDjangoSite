from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext

from books.models import Author, Book


def index(request):
    all_books = Book.objects
    template = loader.get_template('books/index.html')
    context = RequestContext(request, {
        'all_books': all_books,
    })
    return HttpResponse(template.render({}, request))


def author_detail(request, a_id):
    return HttpResponse("Это страничка автора " + Author.objects.all().filter(id=a_id)[0].__str__())


def book_detail(request, b_id):
    return HttpResponse("Это страничка, посвященная книге \"" + Book.objects.all().
                        filter(author__book__id=b_id)[0].__str__() + "\"<br>"
                        + "Потом тут будет ещё описание книги и ссылка на автора."
                        )
