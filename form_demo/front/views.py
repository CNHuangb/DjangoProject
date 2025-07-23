from django.shortcuts import render,HttpResponse
from .forms import MessageBoardFrom, RegisterForm, ArticleForm

from django.views.decorators.http import require_http_methods

# Create your views here.


@require_http_methods(['GET','POST'])
def index(request):
    if request.method == 'GET':
        form = MessageBoardFrom()
        return render(request, 'index.html', context={'form':form})
    elif request.method == 'POST':
        form = MessageBoardFrom(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            return HttpResponse(f"{title},{content},{email}")
        else:
            print(form.errors)
            return HttpResponse("表单验证失败！")
        

@require_http_methods(['GET','POST'])
def register_view(request):
    if request.method == 'GET':

        return render(request, 'register.html')
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            return HttpResponse(telephone)
        else:
            print(form.errors)
            return HttpResponse("表单验证失败！")
        


@require_http_methods(['GET','POST'])
def article_view(request):
    if request.method == 'GET':

        return render(request, 'article.html')
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            return HttpResponse(f"{title},{content}")
            # create_time = form.cleaned_data.get('create_time')
            # return HttpResponse(f"{title},{content},{create_time}")
        else:
            print(form.errors)
            return HttpResponse("表单验证失败！")