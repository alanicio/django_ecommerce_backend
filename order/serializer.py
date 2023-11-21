from rest_framework import serializers
from .models import *


class DiscountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountType
        fields = "__all__"


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
