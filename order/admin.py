from django.contrib import admin
from . import models

admin.site.register(models.DiscountType)
admin.site.register(models.Discount)
admin.site.register(models.Order)
admin.site.register(models.ItemOrder)
