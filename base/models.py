from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    count = models.IntegerField()

class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    total_spent = models.FloatField()
    items = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)