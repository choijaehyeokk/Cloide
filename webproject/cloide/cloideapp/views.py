from django.shortcuts import render

# Create your views here.
def firstpage(request):
    return render(request,'firstpage.html')


#성별에 따른 스타일 이동
def mstyle(request):
    return render(request,'mstyle.html')
def wstyle(request):
    return render(request, 'wstyle.html')

#남자로 이동시 연령대
def mage(request):
    return render(request, 'mage.html')
def mten(request):
    return render(request, 'mten.html')

def mtwenty(request):
    return render(request, 'mtwenty.html')
def mthirty(request):
    return render(request, 'mthirty.html')
def mfourty(request):
    return render(request, 'mfourty.html')

#여자로 이동시 연령대
def wage(request):
    return render(request, 'wage.html')

def wten(request):
    return render(request, 'wten.html')

def wtwenty(request):
    return render(request, 'wtwenty.html')
def wthirty(request):
    return render(request, 'wthirty.html')
def wfourty(request):
    return render(request, 'wfourty.html')



