from django.db import models

class Message(models.Model):
    text1 = models.CharField(max_length=255)
    text2 = models.CharField(max_length=255)
  
    
    def __str__(self):
        return f"{self.text1} {self.text2}"
