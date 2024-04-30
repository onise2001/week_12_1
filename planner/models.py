from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=50)
    descritpion = models.TextField(blank=True)
    date = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
