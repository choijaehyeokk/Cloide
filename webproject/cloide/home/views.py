from django.shortcuts import render,get_object_or_404
from .models import Magazine
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

=======
from brand.models import Brand
>>>>>>> 727601f5c4c76b686d9458fa2fd34bd7ffe7e7e5
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

<<<<<<< HEAD

@login_required
def update(request):
    if request.method == 'POST':
            user_change_form = UserChangeForm(data=request.POST, instance=request.user)
            if user_change_form.is_valid():
                user = user_change_form.save()
                return redirect('update.html',request.user.username)
            else:
                user_change_form = UserChangeForm(instance = request.user)
                return render(request, 'update.html', {'user_change_form':user_change_form})
=======
def search(request):
    query = request.GET['query']
    if query:
        brands = Brand.objects.filter(name__contains=query)
    return render(request,'search.html',{'brands':brands})

def magazine_detail(request,magazine_id):
    magazine_detail = get_object_or_404(Magazine,pk=magazine_id)
    return render(request,'magazine_detail.html',{'magazine':magazine_detail})
>>>>>>> 727601f5c4c76b686d9458fa2fd34bd7ffe7e7e5
