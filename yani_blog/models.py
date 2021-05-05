from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField(blank=True)
    birthday = models.DateTimeField('date published', null=True)
