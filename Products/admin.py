from django.contrib import admin

# Register your models here.
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'farmer', 'quantity', 'unit_price', 'status']  
    list_filter = ['status', 'farmer']  
    search_fields = ['name'] 
    ordering = ['name']  

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product', 'farmer', 'quantity', 'total_price', 'status', 'delivery']
    list_filter = ['status', 'delivery', 'farmer']
    search_fields = ['order_id', 'product__name', 'farmer__first_name']
    ordering = ['order_id']
