from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
from skincare_recommendation_app.models import Product
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import ensure_csrf_cookie

import json
from django.templatetags.static import static
from skincare_recommendation_app import utils

import os

# Create your views here.
def home(request):
    return render(request, 
    "admin/home.html", 
    {
        'name': 'Test',
        'date': datetime.now()
    })

def user_product(request):
     # Get List Product
    products = Product.objects.filter(category__icontains=request.GET.get("category"))

    returnProduct = []
    for product in products:
        temp = {
                'name':product.name, 
                'imagePath':product.image, 
                'description':product.price,
                'price':product.price,
                'review':product.review,
                'defaultImage':'assets/img/Logo-BINUS-University.jpg'
            }
        returnProduct.append(temp)

    returnProduct = Paginator(returnProduct, 6)

    totalData = returnProduct.count
    print("total data product : " + str(totalData))

    pageNum = 1
    if(totalData > 0): 
        pageNum = request.GET.get("page") if request.GET.get("page") else 1

    return JsonResponse({
            'products': list(returnProduct.page(pageNum)),
            'range': list(range(1, returnProduct.page(pageNum).paginator.num_pages + 1))
        })
    
def user_home(request):
    if(request.method=='POST'):
        # Upload User File
        file_name = utils.upload_file(request.FILES.get("inputFile"))

        # get user skin condition 
        user_skin_condition = utils.get_user_skin_condition('skincare_recommendation_app' + static("user/upload/") + file_name)

        # Get List Product
        products = Product.objects.filter(category__icontains=user_skin_condition)

        returnProduct = []
        for product in products:
            temp = {
                    'name':product.name, 
                    'imagePath':product.image, 
                    'description':product.price,
                    'price':product.price,
                    'review':product.review,
                    'defaultImage':'assets/img/Logo-BINUS-University.jpg'
                }
            returnProduct.append(temp)

        returnProduct = Paginator(returnProduct, 6)

        totalData = returnProduct.count
        print("total data product : " + str(totalData))

        pageNum = 1
        if(totalData > 0): 
            pageNum = request.GET.get("page") if request.GET.get("page") else 1

        skinDescription = ""
        if (user_skin_condition == 'Wrinkles') :
            skinDescription = "Wrinkles (Keriput)"
        elif(user_skin_condition == 'Acne'):
            skinDescription = "Acne (Jerawat)"
        elif(user_skin_condition == 'Blackhead'):
            skinDescription = "Blackhead (Komedo)"
        
        return render(request, 
            "public/home.html", 
            {
                'name': 'Test',
                'date': datetime.now(),
                'title': 'Skincare Recommendation',
                'skinDescription': skinDescription,
                'userUploadImage': '/user/upload/' + file_name,
                'userFileName': file_name,
                'productCategory': user_skin_condition,
                'products': returnProduct.page(pageNum),
                'range': range(1, returnProduct.page(pageNum).paginator.num_pages + 1)
            })

    if (request.GET.get("page")):
        # Get List Product
        products = Product.objects.filter(category__icontains=request.GET.get("category"))

        returnProduct = []
        for product in products:
            temp = {
                    'name':product.name, 
                    'imagePath':product.image, 
                    'description':product.price,
                    'price':product.price,
                    'review':product.review,
                    'defaultImage':'assets/img/Logo-BINUS-University.jpg'
                }
            returnProduct.append(temp)

        returnProduct = Paginator(returnProduct, 6)

        totalData = returnProduct.count
        print("total data product : " + str(totalData))

        pageNum = 1
        if(totalData > 0): 
            pageNum = request.GET.get("page") if request.GET.get("page") else 1
        
        skinDescription = ""
        if (request.GET.get("category") == 'Wrinkles') :
            skinDescription = "Wrinkles (Keriput)"
        elif(request.GET.get("category") == 'Acne'):
            skinDescription = "Acne (Jerawat)"
        elif(request.GET.get("category") == 'Blackhead'):
            skinDescription = "Blackhead (Komedo)"

        return render(request, 
            "public/home.html", 
            {
                'name': 'Test',
                'date': datetime.now(),
                'title': 'Skincare Recommendation',
                'userUploadImage': ('/user/upload/' + request.GET.get('fileName')) if request.GET.get('fileName') else None,
                'userFileName': request.GET.get('fileName'),
                'skinDescription': skinDescription,
                'productCategory': request.GET.get("category"),
                'products': returnProduct.page(pageNum),
                'range': range(1, returnProduct.page(pageNum).paginator.num_pages + 1)
            })
    
    return render(request, 
        "public/home.html", 
        {
            'name': 'Test',
            'date': datetime.now(),
            'title': 'Skincare Recommendation',
        })

def category(request):
    return HttpResponse("Hello, This is category!")