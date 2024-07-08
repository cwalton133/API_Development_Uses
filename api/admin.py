from django.contrib import admin
from .models import Item, Supplier, StoreInventory


admin.site.register(Item)
admin.site.register(Supplier)
admin.site.register(StoreInventory)
