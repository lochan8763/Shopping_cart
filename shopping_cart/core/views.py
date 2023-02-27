from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import admin

from .models import User, Product

# Create your views here.
def frontpage(request):
    prod = Product.objects.all()
    return render(request, 'core/frontpage.html',context={'prod': prod})
