from django.urls import path
from . import views


app_name = 'front'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('register', views.register_view, name= 'register_view'),
    path('article', views.article_view, name= 'article_view'),
]
