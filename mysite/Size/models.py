from django.db import models
from polls.models import Products
# Create your models here.
class Size(models.Model):
    size_name = models.ForeignKey(Products,default=None,on_delete=models.CASCADE)
    size_description = models.CharField(max_length=20)
    isactive = models.BooleanField(default=True)
