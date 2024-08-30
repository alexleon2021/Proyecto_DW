from django.db import models

# Create your models here.



class Position(models.Model):
    description = models.CharField(max_length=255, null=False, blank=False)
    
class City(models.Model):
    description = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False)
