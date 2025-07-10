from django.shortcuts import render,HttpResponse

from .models import User, Article

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
