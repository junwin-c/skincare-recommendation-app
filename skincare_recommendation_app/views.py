from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from skincare_recommendation_app.models import Product
from skincare_recommendation_app.models import Category
import os

# Create your views here.
def home(request):
    return render(request, 
    "admin/home.html", 
    {
        'name': 'Test',
        'date': datetime.now()
    })

def userHome(request):
    products = Product.objects.all()
    returnProduct = {}
    for product in products:
        returnProduct.__setattr__(name, value)
        if (product.path_image == ""):
            product.path_image = 'assets/img/Logo-BINUS-University.jpg'
    print(products[0].path_image)

    return render(request, 
    "public/home.html", 
    {
        'name': 'Test',
        'date': datetime.now(),
        'title': 'Skincare Recommendation App',
        'skinDescription': 'kulit anda termasuk berminyak',
        'products': [
            {
                'name':'nama produk',
                'path_image':'assets/img/Logo-BINUS-University.jpg',
                'description':'ini contoh description'
            }, 
            {
                'name':'nama produk',
                'imagePath':'assets/img/Logo-BINUS-University.jpg',
                'description':'ini contoh description'
            },
            {
                'name':'nama produk',
                'imagePath':'assets/img/Logo-BINUS-University.jpg',
                'description':'ini contoh description'
            },
            {
                'name':'nama produk',
                'imagePath':'assets/img/Logo-BINUS-University.jpg',
                'description':'ini contoh description'
            },
            {
                'name':'nama produk',
                'imagePath':'assets/img/Logo-BINUS-University.jpg',
                'description':'ini contoh description'
            },
            {
                'name':'nama produk',
                'imagePath':'assets/img/Logo-BINUS-University.jpg',
                'description':'ini contoh description'
            }
        ]
    })

def category(request):
    return HttpResponse("Hello, This is category!")