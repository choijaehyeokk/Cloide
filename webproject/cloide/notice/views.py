from django.shortcuts import render , get_object_or_404 ,redirect
from .models import Notice
from django.core.paginator import Paginator

from django.utils import timezone
from .forms import NoticeUpdate

#create 혹시 몰라서 만들어 놓음

def create(request):
    notice = Notice()
    notice.title = request.GET['title']
    notice.body = request.GET['body']
    notice.pub_date = timezone.datetime.now()
    notice.save()
    return redirect('/notice/'+ str(notice.id))


def detail(request,notice_id):
    notice_detail = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'detail.html' , {'notice': notice_detail})


def notice(request):
    notices = Notice.objects
     
    notice_list = Notice.objects.all().order_by('-id')

    paginator = Paginator(notice_list,5)
  
    page = request.GET.get('page')

    articles = paginator.get_page(page)

    return render(request, "notice.html", {'notices':notices, 'articles':articles})




