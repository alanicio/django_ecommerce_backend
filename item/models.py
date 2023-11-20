from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    stock = models.IntegerField(null=False)
    price = models.FloatField(null=False)
