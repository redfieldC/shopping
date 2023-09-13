from django.db import models
from polls.models import Products
# Create your models here.
class Colors(models.Model):
    color_name = models.ForeignKey(Products, on_delete=models.CASCADE,default=None)
    color_description = models.CharField(max_length=10)
    isactive = models.BooleanField(default=True)
    
