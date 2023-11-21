from rest_framework import viewsets
from .models import Item
from .serializer import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    """ def retrieve(self, request, *args, **kwargs):
        #todo anything
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data) """
