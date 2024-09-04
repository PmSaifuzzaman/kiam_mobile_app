#model.py

from django.db import models

class Employee(models.Model):
    pf_no = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    territory = models.CharField(max_length=100)
    party_name = models.CharField(max_length=100)
    party_code=models.CharField(max_length=50,default='default_party_code')
    line = models.CharField(max_length=50,default='default_party_code')
 



