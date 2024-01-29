from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def home_page(request):
    return render(request, 'pages/home.html')

def about_page(request):
    return render(request, 'pages/about.html')

def how_page(request):
    return render(request, 'pages/howitworks.html')

def browse_page(request):
    employees = Employee.objects.all()
    return render(request, 'pages/browse.html', {'employees':employees})

def become_page(request):
    return render(request, 'pages/become.html')


def signin_page(request):
    return render(request, 'pages/signin.html')




def signup_page(request):
    
    form = ()
    context = {'form':form}
    return render(request, 'pages/signup.html', context)

def signupsignin_page(request):
    return render(request, 'pages/signin.html')

def signinsignup_page(request):
    return render(request, 'pages/signup.html')
def login_page(request):
    return  HttpResponse("This is Log-in Page")
    