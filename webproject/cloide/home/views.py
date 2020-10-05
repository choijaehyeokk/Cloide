from django.shortcuts import render
from .models import Magazine

# Create your views here.
def home(request):
    magazine = Magazine.objects
    return render(request,'home.html',{'magazines':magazine})

def mypage(request):
    return render(request,'mypage.html')

def intro(request):
    return render(request,'intro.html')

def mycloset(request):
    return render(request,'mycloset.html')