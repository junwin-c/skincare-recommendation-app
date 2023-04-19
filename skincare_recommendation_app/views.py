from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
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