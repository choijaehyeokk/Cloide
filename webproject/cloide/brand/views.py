from django.shortcuts import render, get_object_or_404,redirect
from .models import Brand, Agesex, Stylekind,User_brand_add,Yvideo
from django.contrib.auth.models import User
from urllib import parse

# Create your views here.


def brand_detail(request):
    #brand = Brand.objects.bnum
    #brand.bnum = request.POST['bnum']
    yobject =  Yvideo.objects.all()
    current_url = request.get_full_path()
    temp = current_url.split('?')
    print(temp)
    brand = temp[1]
    dec = parse.unquote(brand)

    allbrand = Brand.objects.all()
    result = list()
    for choice in allbrand:
        if dec == choice.name:
            #상세페이지 브랜드랑 db내 브랜드와 같다면
            result.append(choice)
    
    print(result)#result에 해당 브랜드의 정보 담아서 상세페이지로 전달.
   
    #brand = request.POST.get('brand_name')
    return render(request, 'brand_detail.html',{'brand':result,'yvideo':yobject})

def brand(request):
    brand = Brand.objects.all()
    agesex = Agesex.objects.all()
    stylekind = Stylekind.objects.all()
    current_url = request.get_full_path()
    token = current_url.split('?')
    sex = token[1]
    if sex == 'Man':sex=1
    else : sex=0
    style = token[2]
    age = int(token[3])
    brandlist = list()
    result = list()
    for b in brand:
        for a in agesex:
            if b.bnum == a.brand.bnum and age == a.age and sex == a.sex:
                brandlist.append(b)
    if style == 'All' : style = 0
    elif style =='Suit' : style = 16
    elif style == 'Sport' : style =8
    elif style == 'Casual' : style = 1
    elif style == 'Vintage' : style = 3
    elif style == 'Street' : style = 4
    
    for b in brandlist:
        for s in stylekind:
            if b.bnum == s.brand.bnum and s.style == style:
                result.append(b)
            elif style == 0:
                result = brandlist
                break
    print(result)

    #1. views 안에서 모든 처리, html에서는 쿼리해서 받아온 브랜드들을 보여주기만한다.
    #2. 토큰을 html에 넘겨줘서 html안에서 모델에 접근해서 보여준다.
    return render(request,'brand.html',{'current_url' : current_url, 'brands' : result})

def user_brand_add(request):
    u_object = User_brand_add.objects.all()
    
    allbrand = Brand.objects.all()
    if(request.user.is_authenticated):
      current_user_name = request.user.username
    
    for choice in allbrand:
       if b.name == choice.name:
           current_brand_bnum = b.bnum
           result.append(choice)

    u_object.user_name = current_user_name
    u_object.current_brand = current_brand_bnum
    u_object.save()

    return redirect('/')