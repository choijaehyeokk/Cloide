from django.shortcuts import render

# Create your views here.
def firstpage(request):
    return render(request,'firstpage.html')

def mstyle(request):
    return render(request,'mstyle.html')

def mage(request):
    return render(request, 'mage.html')

def mten(request):
    return render(request, 'mten.html')