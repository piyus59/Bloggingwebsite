from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=50)


class Blog(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    text = models.TextField()
    creation_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    





