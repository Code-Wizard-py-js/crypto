from django.db import models
import datetime,pytz
from django.utils import timezone
# Create your models here.
print(timezone.now)
from unixtimestampfield.fields import UnixTimeStampField
def newtime():
    now = datetime.datetime.now()
    timestamp = datetime.datetime.timestamp(now)
    return timestamp
class Sivan(models.Model):
    
    sivanna=models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.updated_at)
class Forest(models.Model):
    
    Forest=models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.updated_at)

class Arctic(models.Model):
    
   
    Arctic=models.TextField(blank=True)
    updated_at =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.updated_at)

class Mystic(models.Model):
    
    Mystic=models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.updated_at)

class Genesis(models.Model):
    
    Genesis=models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.updated_at)
