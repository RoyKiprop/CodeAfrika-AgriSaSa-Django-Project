from django.contrib import admin

# Register your models here.

from .models import Transactions


@admin.register(Transactions)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'transaction_type']
    list_filter = ['transaction_type', 'account']
    search_fields = ['account__account_number']
    ordering = ['account']

