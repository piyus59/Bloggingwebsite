from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    text = models.TextField()
    creation_time = models.DateTimeField(auto_now=True)
    category = [
        ('CA', 'Computer Apllication'),
        ('CS', 'Computer Science'),
        ('MC', 'Machanical'),
        ('EL', 'Electrical'),
    ]
    category = models.CharField(
        max_length=2,
        choices=category,
        default='CA',
    )


