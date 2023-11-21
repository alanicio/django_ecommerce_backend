from rest_framework import viewsets
from .models import Item
from .serializer import ItemSerializer
import logging


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        search = self.request.query_params.get("search")
        logger = logging.getLogger("mylogger")
        logger.info(self.request.query_params)
        if search is not None:
            queryset = queryset.filter(name=search)
        return queryset
