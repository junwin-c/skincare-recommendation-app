from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def category(request):
    return HttpResponse("Hello, This is category!")