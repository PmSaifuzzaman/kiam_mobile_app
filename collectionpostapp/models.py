# collectionpostapp/models.py

from django.db import models

class CollectionPost(models.Model):
    date = models.DateField()
    pf_no = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=100)
    party_name = models.CharField(max_length=100)
    party_code = models.CharField(max_length=50)
    account_no = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.employee_name}"
