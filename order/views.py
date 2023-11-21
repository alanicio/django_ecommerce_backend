from rest_framework import viewsets
from .models import *
from .serializer import *


class DiscountTypeViewSet(viewsets.ModelViewSet):
    queryset = DiscountType.objects.all()
    serializer_class = DiscountTypeSerializer


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
