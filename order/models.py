from django.db import models


class DiscountType(models.Model):
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    enum = models.CharField(max_length=50, null=True)


class Discount(models.Model):
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    type = models.CharField(max_length=100, null=False)
    discount_quantity = models.IntegerField(null=False)
    discount_type = models.ForeignKey(DiscountType, on_delete=models.CASCADE)
    quantity_critera = models.IntegerField(null=True)
    amount_criteria = models.IntegerField(null=True)


class Order(models.Model):
    country = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    neighborhood = models.CharField(max_length=200, null=False)
    street = models.CharField(max_length=200, null=False)
    exterior_number = models.CharField(max_length=10, null=False)
    interior_number = models.CharField(max_length=10, null=True)
    subtotal = models.FloatField(null=False)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    total = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
