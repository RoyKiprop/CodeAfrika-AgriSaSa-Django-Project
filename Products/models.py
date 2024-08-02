from django.db import models
from Farmers.models import Farmer

# Create your models here.
class Product(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.CharField(max_length=20)
    STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Approved'),
        (2, 'Rejected'),
    ]
    status = models.IntegerField( choices=STATUS_CHOICES, default='pending')

class Order(models.Model):
    STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Paid'),
        (2, 'Cancelled'),
    ]
    
    DELIVERY_CHOICES = [
        (0, 'Packaging'),
        (1, 'Shipped'),
        (2, 'Delivered'),
    ]
    
    order_id = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    delivery = models.IntegerField(choices=DELIVERY_CHOICES, default=0)
