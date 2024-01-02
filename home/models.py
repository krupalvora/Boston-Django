from django.db import models
from django.db.models.expressions import Value
from rest_framework import serializers
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Store(models.Model):
    book_id = models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    book_name=models.CharField(max_length=200)
    price=models.IntegerField()

    def __str__(self):
    	return self.book_id
    
