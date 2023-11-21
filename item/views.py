from rest_framework import viewsets
from .models import Item
from .serializer import ItemSerializer
from django.db.models import Q


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        search = self.request.query_params.get("search")
        if search is not None:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )
        return queryset
