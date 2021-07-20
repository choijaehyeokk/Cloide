from django.shortcuts import render, get_object_or_404,redirect
from brand.models import Brand, Agesex, Stylekind,User_brand_add,Yvideo
from django.contrib.auth.models import User
from urllib import parse
##
def menubrand(request):
    brand = Brand.objects.all() #브랜드 db 호출
    agesex = Agesex.objects.all() #성별, 연령대 db 호출
    stylekind = Stylekind.objects.all() #스타일 db호출 
    current_url = request.get_full_path() #메뉴바 연령대, 스타일을 저장한 url
    token = current_url.split('?') #분리해서 연령대와 스타일 파악
    style = token[2]
    age = int(token[1])
    brandlist = list()
    result = list()
    for b in brand:
        for a in agesex:
            if b.bnum == a.brand.bnum and age == a.age:#연령대까지만
                brandlist.append(b)
    if style == 'cas' : style = 1
    elif style =='str' : style = 4
    elif style == 'mod' : style = 5
    elif style == 'nom' : style = 2
    elif style == 'min' : style = 6
    elif style == 'cla' : style = 7
    elif style == 'spo' : style = 8
    elif style == 'nat' : style = 9
    elif style == 'gla' : style = 12
    elif style == 'chi' : style = 13
    elif style == 'formal' : style = 10
    elif style == 'vin' : style = 3
    elif style == 'ame' : style = 17
    elif style == 'dan' : style = 16


    for b in brandlist:
        for s in stylekind:
            if b.bnum == s.brand.bnum and s.style == style:
                if b not in result:
                    result.append(b)
            elif style == 0:
                result = brandlist
                break
    print(result)

    #1. views 안에서 모든 처리, html에서는 쿼리해서 받아온 브랜드들을 보여주기만한다.
    #2. 토큰을 html에 넘겨줘서 html안에서 모델에 접근해서 보여준다.
    return render(request,'brand.html',{'current_url' : current_url, 'brands' : result})

##