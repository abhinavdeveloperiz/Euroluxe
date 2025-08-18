from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def Products(request):
    return render(request,'product.html')

from django.views.decorators.cache import cache_page

def About(request):
    return render(request,'about.html')


def Contact(request):
    return render(request,'contact.html')