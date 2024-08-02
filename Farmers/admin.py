from django.contrib import admin

# Register your models here.
from .models import Farmer, Account

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']
    list_filter = ['first_name']
    search_fields = ['first_name', 'email', 'location']
    ordering = ['first_name']

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_no', 'farmer', 'actual_balance', 'available_balance', 'account_type']
    list_filter = ['account_type', 'farmer']
    search_fields = ['account_no', 'farmer__first_name', 'farmer__last_name']
    ordering = ['account_no']


