from tkinter import CASCADE
from django.db import models

from categories.models import Categories

# Create your models here.
class SUBCategories(models.Model):
    category_name = models.ForeignKey(Categories,on_delete=models.CASCADE)
    sub_categories_name = models.CharField(max_length=20)
    sub_categories_description = models.CharField(max_length=20)
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return self.categories_name 


    
