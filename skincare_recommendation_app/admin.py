from django.contrib import admin
from django_stisla.admin import site
from .models import Product
from .models import Category

# Register your models here.
site.register(Product)
site.register(Category)