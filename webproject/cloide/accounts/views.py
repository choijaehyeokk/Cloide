from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
##유저 정보 수정 기능##
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordCheck']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html' , {'error' : "입력하신 아이디가 이미 존재합니다"})
            except:

                user = User.objects.create_user(
                    username=request.POST["username"], password = request.POST["password"])
                auth.login(request,user)
                return redirect('/home')
            
        else:
           return render(request, 'signup.html' , {'error' : "비밀번호가 맞지 않습니다."}) 
    else:
        return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            return render(request,'login.html', {'error': "아이디나 비밀번호가 유효하지 않습니다."})
    else:
        return render(request, "login.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("/home")
    else:
        return render(request, 'signup.html')


####유저 정보 수정 기능###

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


def oauth(request):
    code = request.GET['code']
    print('code ='+ str(code))
    return redirect('login')



def kakao_login(request):
    login_request_uri = 'http://kauth.kakao.com/oauth/authorize?'

    client_id = 'cf7b5b5200d48061f32d906759bbff87'
    redirect_uri = 'http://127.0.0.1:8000/oauth/'

    login_request_uri += 'client_id=' + client_id
    login_request_uri += '&redirect_uri=' + redirect_uri
    login_request_uri += '&response_type=code'

    return redirect(login_request_uri)
