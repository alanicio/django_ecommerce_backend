from rest_framework import serializers

from item.serializer import ItemSerializer
from .models import *
import logging

logger = logging.getLogger("mylogger")


class DiscountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountType
        fields = "__all__"


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(read_only=True, many=True)
    subtotal = serializers.FloatField(required=False)
    total = serializers.FloatField(required=False)
    interior_number = serializers.CharField(allow_blank=True)

    class Meta:
        model = Order
        fields = "__all__"
        optional_fields = ["total", "subtotal", "interior_number"]

    def getSubtotal(self, items):
        logger.info("------ITEMS------")
        logger.info(repr(items))
        subtotal = 0
        for item in items:
            amount = item.quantity * item.price
            subtotal += amount
        return subtotal

    def create(self, validated_data):
        request = self.context["request"]
        logger.info("REQUEST")
        logger.info(repr(request.data))
        logger.info(repr(request.data.get("items")))
        subtotal = self.getSubtotal(request.data.get("items"))
        validated_data.total = subtotal
        validated_data.subtotal = subtotal
        logger.info("------VALIDATED DATA------")
        logger.info(repr(validated_data))
        instance = super().create(validated_data)
        return instance

    def get_validation_exclusions(self):
        exclusions = super(OrderSerializer, self).get_validation_exclusions()
        return exclusions + ["subtotal", "total"]
