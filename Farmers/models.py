from django.db import models

class Farmer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    isActive = models.IntegerField(default=False)
    isStaff = models.IntegerField(default=False)
    PLAN_CHOICES = [
        (0, 'Basic'),
        (1, 'Pro'),
       
    ]
    plan = models.IntegerField(choices=PLAN_CHOICES, default=0)
    location = models.CharField(max_length=30)

    
class Account(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        (0, 'Farmer'),
        (1, 'Business'),
    ]

    account_no = models.IntegerField(max_length=10, unique=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    actual_balance = models.DecimalField(max_digits=15, decimal_places=2)
    available_balance = models.DecimalField(max_digits=15, decimal_places=2)
    account_type = models.IntegerField(choices=ACCOUNT_TYPE_CHOICES, default=0)

    

