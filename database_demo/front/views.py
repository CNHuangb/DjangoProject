from django.shortcuts import render,HttpResponse

from django.db.models import Avg, Count, Max, Min, Sum, F, Q
from .models import Book, BookOrder, Publisher, Author


import asgiref.sync


# Create your views here.


def avg_view(request):
    result = Book.objects.aggregate(avg_price = Avg('price'))

    print(result)

    return HttpResponse("Avg view")



def count_view(request):
    result = Book.objects.aggregate(book_count = Count('id'))

    print(result)

    return HttpResponse("Count view")


def max_min_view(request):
    result = Author.objects.aggregate(max_age = Max('age'), min_age = Min('age'))

    print(result)

    return HttpResponse("Max Min view")


def sum_view(request):
    result = Book.objects.annotate(total = Sum("bookorder__price")).values('name','total')

    print(result)

    return HttpResponse("Sum view")


def f_view(request):
    Book.objects.update(price = F('price') - 10)

    return HttpResponse("F view")


def q_view(request):
    books = Book.objects.filter(Q(price__gte=80) | Q(rating__gte=9)).all()

    for book in books:
        print(book.name, book.price, book.rating)

    return HttpResponse("Q view")