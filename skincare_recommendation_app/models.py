from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    ingridients = models.TextField()
    diseases = models.TextField()
    path_image = models.CharField(max_length=120)

class Category(models.Model):
    name = models.CharField(max_length=120)