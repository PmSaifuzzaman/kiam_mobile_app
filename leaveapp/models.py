# models.py
from django.db import models

class Leave(models.Model):
    pfNo = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    days = models.IntegerField()
    leaveType = models.CharField(max_length=20, blank=True)
    description = models.TextField()
