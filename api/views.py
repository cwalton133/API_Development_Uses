from rest_framework import generics
from .models import Item, StoreInventory, Supplier
from .serializers import ItemSerializer, SupplierSerializer, StoreInventorySerializer

class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class SupplierListCreateAPIView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class StoreInventoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = StoreInventory.objects.all()
    serializer_class = StoreInventorySerializer


class StoreInventoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreInventory.objects.all()
    serializer_class = StoreInventorySerializer
