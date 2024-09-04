# orderapp/models.py

from django.db import models

class Order(models.Model):
    date = models.DateField()
    pf_no = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    party_name = models.CharField(max_length=100)
    party_code = models.CharField(max_length=100)
    total_order_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=100,default='default_descrip')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()


