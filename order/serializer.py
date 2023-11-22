from rest_framework import serializers
from item.serializer import ItemSerializer
from .models import *


class DiscountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountType
        fields = "__all__"


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"


class ItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOrder
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(read_only=True, many=True)
    subtotal = serializers.FloatField(required=False)
    total = serializers.FloatField(required=False)
    interior_number = serializers.CharField(allow_blank=True)
    itemOrders = ItemOrderSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Order
        fields = "__all__"
        optional_fields = ["total", "subtotal", "interior_number"]

    def getSubtotal(self, items):
        subtotal = 0
        for item in items:
            amount = item["quantity"] * item["price"]
            subtotal += amount
        return subtotal

    def create(self, validated_data):
        request = self.context["request"]
        items = request.data.get("items")
        subtotal = self.getSubtotal(items)
        validated_data["total"] = subtotal
        validated_data["subtotal"] = subtotal
        order = Order.objects.create(**validated_data)
        for itemIteration in items:
            quantity = itemIteration.pop("quantity")
            item, created = Item.objects.get_or_create(**itemIteration)
            ItemOrder.objects.create(order=order, quantity=quantity, item=item)
        return order

    def get_validation_exclusions(self):
        exclusions = super(OrderSerializer, self).get_validation_exclusions()
        return exclusions + ["subtotal", "total", "itemOrders"]
