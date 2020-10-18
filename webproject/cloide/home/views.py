from django.shortcuts import render,get_object_or_404
from .models import Magazine
from brand.models import Brand

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

def search(request):
    query = request.GET['query']
    if query:
        brands = Brand.objects.filter(name__contains=query)
    return render(request,'search.html',{'brands':brands})

def magazine_detail(request,magazine_id):
    magazine_detail = get_object_or_404(Magazine,pk=magazine_id)
    return render(request,'magazine_detail.html',{'magazine':magazine_detail})

