from django.shortcuts import render
from .models import Magazine

# Create your views here.
def home(request):
    magazine = Magazine.objects
    return render(request,'home.html',{'magazines':magazine})