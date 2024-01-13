from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Branch(models.Model):
    name = models.CharField(max_length=255)
    # Add other branch-related fields as needed

class Accounting(models.Model):
    in_amount = models.DecimalField(max_digits=10, decimal_places=2)
    out_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    # Add other accounting-related fields as needed
# Add more models as needed for branches, accounting, etc.

