"""
URL configuration for helloworld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import HttpResponse
from book import views

from django.urls import reverse


def index(request):

    # print(reverse("book_detail_query_string"))

    # /book/str/1
    # print(reverse(viewname="book_str", kwargs={"book_id":1}))

    # /book?id=1,字符串拼接的方式
    # print(reverse(viewname="book_detail_query_string") + "?id=1")



    print(reverse(viewname="movie:movie_list"))




    return HttpResponse("欢迎来到知了课堂！")


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('book', views.book_detail_query_string, name= "book_detail_query_string"),

    path('book/<book_id>', views.book_detail_path),
    path('book/str/<str:book_id>', views.book_str, name="book_str"),

    path('book/slug/<slug:book_id>', views.book_slug, name="book_slug"),

    path('book/path/<path:book_id>', views.book_path, name="book_path"),




    path('movie/', include("movie.urls")),

]
