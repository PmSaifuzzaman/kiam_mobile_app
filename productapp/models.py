from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    uom = models.CharField(max_length=50,default='default_uom')
    line = models.CharField(max_length=50,default='default_line')
