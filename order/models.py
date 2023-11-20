from django.db import models


class DiscountTypes(models.Model):
    description = models.TextField(null=true)
    created_at = models.DateTimeField(auto_now_add=True, null=false)
    enum = models.CharField(max_length=50, null=true)

class Discount(models.Model):
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=true)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=true)
    type = models.CharField(, max_length=100, null=false)
  """ discount_quantity integer [not null]
  discount_type_id integer [not null]
  quantity_critera integer [null]
  amount_criteria integer [null] """

class Order(models.Model):
    country = models.CharField(max_length=200, null=false)
    city = models.CharField(max_length=200, null=false)
    neighborhood = models.CharField(max_length=200, null=false)
    street = models.CharField(max_length=200, null=false)
    exterior_number = models.CharField(max_length=10, null=false)
    interior_number = models.CharField(max_length=10, null=true)
    subtotal = models.FloatField(null=false)
    discount_id = models.ForeignKey(Discount, on_delete=models.CASCADE)
    total = models.FloatField(null=false))
    created_at = models.DateTimeField(auto_now_add=True, null=false)
