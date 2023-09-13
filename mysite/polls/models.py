from tkinter import CASCADE
from django.db import models
# Create your models here.
class Products(models.Model):
    Categories = models.CharField(max_length=15)
    sub_categories = models.CharField(max_length=15)
    Colors = models.CharField(max_length=15)
    Size = models.CharField(max_length=15)
    image = models.ImageField(upload_to = 'media/',width_field=None,height_field=None,null=True)
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    sku_number = models.CharField(max_length=10)
    prod_details = models.CharField(max_length=300)
    quantity = models.IntegerField(default=0)
    isactive = models.BooleanField(default=True)
    
    