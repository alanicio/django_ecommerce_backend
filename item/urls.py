from django.urls import path, include
from rest_framework import routers
from item import views

router = routers.DefaultRouter()
router.register(r"items", views.ItemViewSet)

urlpatterns = [path("", include(router.urls))]
