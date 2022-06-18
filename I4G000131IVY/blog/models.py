from django.db import models
from turtle import title
from django.contrib.auth import get_user_model
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
    Title= models.CharField(max_length=200)
    Text= models.TextField()
    Author= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_Date = models.DateTimeField()
    Published_Date = models.DateTimeField()
