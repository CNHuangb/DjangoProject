from django.shortcuts import render, HttpResponse

# Create your views here.


# 在URL中带参数
# 1.通过查询字符串 query string
# 2.在path中携带


def book_detail_query_string(request):
    
    book_id = request.GET.get('id')
    name = request.GET.get('name')

    return HttpResponse(f"您查找的图书ID是：{book_id},图书名称是：{name}")


def book_detail_path(request, book_id):
    return HttpResponse(f"您查找的图书ID是：{book_id}")


def book_str(request, book_id):
    return HttpResponse(f"您查找的图书ID是：{book_id}")


def book_slug(request, book_id):
    return HttpResponse(f"您查找的图书ID是：{book_id}")


def book_path(request, book_id):
    return HttpResponse(f"您查找的图书ID是：{book_id}")