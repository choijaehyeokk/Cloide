from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('mypage/',views.mypage,name='mypage'),
    path('intro/',views.intro,name='intro'),
    path('mycloset/',views.mycloset,name='mycloset'),
    path('search/',views.search,name='search'),
    path('<int:magazine_id>/',views.magazine_detail, name='magazine_detail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)