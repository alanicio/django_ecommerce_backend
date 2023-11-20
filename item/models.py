from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200, null=false)
    description = models.TextField(null=true)
    stock = models.IntegerField(null=false)
    price = models.FloatField(null=false)
