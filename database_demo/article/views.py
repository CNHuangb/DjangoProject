from django.shortcuts import render,HttpResponse

from .models import User, Article
from datetime import datetime

# Create your views here.

def article_test(request):

    # user = User(username = '知了', password = '111111')
    # user.save()

    # article = Article(title = 'chatGPT 5已经发布', content = 'xxx', author = user)

    # article.save()


    article = Article.objects.first()


    print(article.author.username)


    return HttpResponse(article.author.username)


def one_to_many(request):
    user = User.objects.first()

    # articles = user.articles.all()

    articles = user.articles.filter(title__contains = 'chat').all()

    for article in articles:
        print(article.title)

    return HttpResponse("成功！")


def query1(request):
    # article = Article.objects.filter(id__exact = 1)


    article = Article.objects.filter(title__iexact = 'chatGPT 5已经发布')

    print(article.query)
    print(article)

    return HttpResponse("查询成功！")


def query2(request):

    # article = Article.objects.filter(title__contains = 'chat')
    article = Article.objects.filter(title__icontains = 'Chat')

    print(article.query)
    print(article)

    return HttpResponse("查询2成功！")



def query3(request):

    # article = Article.objects.filter(title__contains = 'chat')
    article = Article.objects.filter(id__in = [1,2,3])

    print(article.query)
    print(article)

    return HttpResponse("查询3成功！")


def query4(request):

    start_date = datetime(year=2024, month=4, day=1)
    end_date = datetime(year=2025, month=7, day=11)

    article = Article.objects.filter(pub_time__range = (start_date,end_date))

    print(article.query)
    print(article)

    return HttpResponse("查询4成功！")


def query5(request):

    user = User.objects.filter(articles__title__icontains = 'chat')

    print(user.query)
    print(user)

    return HttpResponse("查询5成功！")