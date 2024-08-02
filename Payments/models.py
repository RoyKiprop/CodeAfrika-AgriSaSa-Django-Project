from django.db import models
from Farmers.models import Farmer, Account

# Create your models here.


class Transactions(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        (0, 'Deposit'),
        (1, 'Withdrawal'),
        (2, 'Commission'),
        (3, 'Subscription'),
        (4, 'Orders'),
    ]
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE_CHOICES, default=0)