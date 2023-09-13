from django.db import models


# Create your models here.
class Categories(models.Model):
    #made changes to category_name for null and blank
    category_name = models.CharField(max_length=10)
    category_description = models.CharField(max_length=10)
    isactive = models.BooleanField(default=True)
    