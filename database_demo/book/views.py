from django.shortcuts import render,HttpResponse

from django.db import connection
from .models import Book,Tag

# Create your views here.



def index(request):
    cursor = connection.cursor()

    cursor.execute("select * from book_book")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    return HttpResponse("查找成功")


def add_book(request):
    book = Book(name='三国演义', author='罗贯中', price=100 )
    book.save()


    # book = Book(name='西游记', author='吴承恩', price=100 )
    # book.save()

    return HttpResponse("图书插入成功")


def query_book(request):
    books = Book.objects.all()



    # books = Book.objects.filter(name='三国演义')
    
    for book in books:
        print(book.id, book.author, book.pub_time, book.price)

    # try:
    #     book = Book.objects.get(name='三国演义')
    #     print(book.name)
    # except Book.DoesNotExist:
    #     print("图书不存在")

    return HttpResponse("图书查询成功")





def order_view(request):

    # books = Book.objects.order_by('-pub_time')


    books = Book.objects.all()
    
    for book in books:
        print(book.id, book.author, book.pub_time, book.price)

    return HttpResponse("排序成功")



def update_view(request):

    book = Book.objects.first()
    
    book.name = "水浒传"
    book.save()

    return HttpResponse("更新成功")


def delete_view(request):

    book = Book.objects.filter(name = '水浒传')
    
    book.delete()

    return HttpResponse("删除成功")


def book_tag(request):
    tag = Tag()
    tag.save()

    return HttpResponse("tag保存成功")
