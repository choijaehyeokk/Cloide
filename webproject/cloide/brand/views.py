from django.shortcuts import render
from .models import Brand, Agesex, Stylekind
# Create your views here.


def brand_detail(request):
    brand = request.POST.get('brand_name')
    return render(request, 'brand_detail.html',)

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

