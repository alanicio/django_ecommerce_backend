from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    stock = models.IntegerField()
    price = models.FloatField()
