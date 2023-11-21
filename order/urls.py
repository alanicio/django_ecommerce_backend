from django.urls import path, include
from rest_framework import routers
from order import views

router = routers.DefaultRouter()
router.register(r"orders", views.OrderViewSet)
router.register(r"discounts", views.DiscountViewSet)

urlpatterns = [path("", include(router.urls))]
