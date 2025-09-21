from django.shortcuts import render
from .models import Home,Testimonial,Product_details
# Create your views here.


def home(request):
    data=Home.objects.order_by("-id").first()
    context={
        "data":data,
    }
    return render(request, 'home.html',context)


def Products(request):
    return render(request,'product.html')

from django.views.decorators.cache import cache_page

def About(request):
    return render(request,'about.html')


def Contact(request):
    return render(request,'contact.html')