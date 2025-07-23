from django.db import models
from django.core import validators

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200, validators=[validators.MinLengthValidator(limit_value=2)])
    content = models.TextField(validators=[validators.MinLengthValidator(limit_value=3)])
    create_time = models.DateTimeField(auto_now_add=True)

    category = models.CharField(max_length=100,blank=False)
