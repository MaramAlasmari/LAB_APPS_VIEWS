from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 
# Create your views here.

def home(request : HttpRequest):

 return render(request,'cars_rental/home.html')


def about (request : HttpRequest):
    return 