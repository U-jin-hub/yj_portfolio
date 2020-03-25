from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'portfolio/home.html')

def hw1(request):
    return render(request,'portfolio/hw1.html')   
 
def review(request):
    return render(request,'portfolio/review.html')     

def new(request):
    return render(request,'portfolio/new.html')  
    