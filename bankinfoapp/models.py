#model.py

from django.db import models

class Bank(models.Model):
    bank_code=models.CharField(max_length=50)
    bank_name = models.CharField(max_length=100)
    account_no = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

   
   