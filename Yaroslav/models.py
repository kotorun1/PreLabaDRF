from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'

    def __str__(self):
        return f"{self.name}: {self.price}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name_plural = 'Carts'
        verbose_name = 'Cart'

    def __str__(self):
        return f"Cart {self.id}"

class Order(models.Model):
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Orders'
        verbose_name = 'Order'

    def __str__(self):
        return f"Order {self.id}: {self.total_price}"
