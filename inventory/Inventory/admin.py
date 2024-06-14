from django.contrib import admin

# Register your models here.
from .models import Product, Stock, Supplier

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Stock)

