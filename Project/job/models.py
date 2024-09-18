from django.db import models

from core.models import City, Company, Position

# Create your models here.
#Modalidad
class Mode(models.Model):
    description = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.description}"

#Habilidades
class Skills(models.Model):
    description = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.description}"
    

class Job(models.Model):
    title = models.CharField(max_length=30)
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    description = models.TextField(max_length=1500, null=True, blank=True)
    def __str__(self):
        return f"{self.title}"


