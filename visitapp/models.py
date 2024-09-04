# visitapp/models.py

from django.db import models
from django.utils import timezone

class Visit(models.Model):
    date = models.DateField()
    pf_no = models.CharField(max_length=100)
    dealer_code = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    outlet = models.CharField(max_length=100)
    start_time = models.TimeField(null=True, default=timezone.now().strftime("%H:%M:%S"))
    end_time = models.TimeField(null=True, default=timezone.now().strftime("%H:%M:%S"))
    visit_type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Set start_time and end_time to the current time if not provided
        if not self.start_time:
            self.start_time = timezone.now().strftime("%H:%M:%S")
        if not self.end_time:
            self.end_time = timezone.now().strftime("%H:%M:%S")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} - {self.outlet}"

