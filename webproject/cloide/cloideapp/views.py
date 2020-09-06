from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def mstyle(request):
    return render(request,'mstyle.html')

def mage(request):
    return render(request, 'mage.html')

def mten(request):
    return render(request, 'mten.html')