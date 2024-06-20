from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Uzdrowisko(models.Model):

    positionx = models.FloatField()
    positiony = models.FloatField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    link = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    rating = models.FloatField()
    details =  models.CharField(max_length=2000)

    def __str__(self):
        return self.name
    
    
class Opinion(models.Model):
    uzdrowisko = models.ForeignKey(Uzdrowisko, related_name='opinions', on_delete=models.CASCADE)
    text = models.TextField()
    