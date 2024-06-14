from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    initial_stock_level = models.IntegerField()

    def __str__(self):
        return self.name

class Stock(models.Model):
    TYPE_CHOICES= {
            "in": "in",
            "out": "out",
            }
    stock_id = models.CharField(primary_key=True, max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)

    def __str__(self):
        return f"name: {self.product.name}, type: {self.type}, quantity: {self.quantity}"

class Supplier(models.Model):
    supplier_id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    products_supplied = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"name: {self.name} contact_info: {self.contact_info}"

class User(models.Model):
    ROLE_CHOICES = {
            "admin": "admin",
            "user": "user",
            }
    user_id = models.CharField(primary_key=True, max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username

