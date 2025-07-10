from django.shortcuts import render,HttpResponse

from datetime import datetime

# Create your views here.


def index(request):
    return render(request, "index.html")



def baidu(request):
    return render(request, "baidu.html")



def info(request):


    # # 1.普通变量
    # username = "知了课堂"

    # return render(request, "info.html", context={"username":username})

    # # 2.字典类型
    # username = "知了课堂"
    # book = {"name":"水浒传","author":"施耐庵"}

    # return render(request, "info.html", context={"username":username,"book":book})


    # # 3.列表类型
    # username = "知了课堂"
    # book = {"name":"水浒传","author":"施耐庵"}
    
    # books = [

    #     {"name":"水浒传","author":"施耐庵"},
    #     {"name":"西游记","author":"吴承恩"}

    # ]

    # context = {
    #     "username":username,
    #     "book":book,
    #     "books":books
    # }

    # return render(request, "info.html", context=context)


    # 4.渲染模型，对象
    username = "知了课堂"
    book = {"name":"水浒传","author":"施耐庵"}
    
    books = [

        {"name":"水浒传","author":"施耐庵"},
        {"name":"西游记","author":"吴承恩"}

    ]

    class Person:
        def __init__(self,realname):
            self.realname = realname



    context = {
        "username":username,
        "book":book,
        "books":books,
        "person":Person("知了课堂")

    }

    return render(request, "info.html", context=context)



def if_view(request):

    age = 18

    return render(request, "if.html", context={"age":age})


def for_view(request):

    # 1.列表 
    books = [

        {"name":"水浒传","author":"施耐庵"},
        {"name":"西游记","author":"吴承恩"}

    ]

    # 2.字典
    person = {
        "realname":"知了课堂",
        "age":18,
        "height":168,

    }

    context = {

        "books":books,
        "person":person


    }

    return render(request, "for.html", context=context)


def with_view(request):
    context = {

        "books":[

        {"name":"水浒传","author":"施耐庵"},
        {"name":"西游记","author":"吴承恩"}

    ]


    }


    return render(request, "with.html", context=context)


def url_view(request):

    return render(request, "url.html")


def book_detail(request,book_id):

    return HttpResponse(f"您访问的图书ID是：{ book_id }")


def filter_view(request):

    greet = "Hello World, Hello django"

    context = {

        "greet" :greet,
        "birthday": datetime.now(),
        "profile": "",
        "html":"<h1>欢迎来到知了课堂</h1>"

    }

    return render(request, "filter.html",context=context)



def template_form(request):

    context = {
        'articles':['小米su7','chatGPT 5发布']

    }

    return render(request, "xfz_index.html", context = context)



def static_view(request):

    return render(request, "static.html")