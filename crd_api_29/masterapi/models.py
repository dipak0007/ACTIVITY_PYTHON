from django.db import models

# Create your models here.
class MyBookModel(models.Model):
    book = models.CharField(max_length=100)
    msg = models.TextField(max_length=500)
    stoke = models.IntegerField(max_length=100)
