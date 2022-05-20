from unicodedata import name
from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=32)
    #certificate_pdf = models.FileField( null=True, blank=True)

    def __str__(self):
        return self.name



    
