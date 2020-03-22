from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'portfolio/home.html')

def hw1(request):
    return render(request,'portfolio/hw1.html')   
    
     