# models.py
from django.db import models

class Payslip(models.Model):
    pfNo = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    payslipType = models.CharField(max_length=20, blank=True)
    pdf_file = models.FileField(upload_to='pdf_files/', null=True, blank=True)

    
