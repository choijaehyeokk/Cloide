from django.shortcuts import render
from .models import Magazine
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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