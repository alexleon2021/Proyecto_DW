from django.db import models

# Create your models here.
class Mode(models.Model):
    description = models.CharField(max_length=20)


class Skills(models.Model):
    description = models.CharField(max_length=30)

class Job(models.Model):
    title = models.CharField(max_length=30)
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE)
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    description = models.TextField(max_length=1500)
