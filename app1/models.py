from django.db import models

# Create your models here.
class TableData(models.Model):
    name=models.CharField(max_length=25)
    department=models.CharField(max_length=25)
    pf_no=models.IntegerField()

class Meta:
    app_label = 'app1'
