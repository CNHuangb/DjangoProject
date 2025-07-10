from django.urls import path
from . import views


app_name = 'article'


urlpatterns = [
    path('test', views.article_test, name="article_test"),
    path('onetomany', views.one_to_many, name="one_to_many"),

]