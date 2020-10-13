from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('mypage/',views.mypage,name='mypage'),
    path('intro/',views.intro,name='intro'),
    path('mycloset/',views.mycloset,name='mycloset'),
<<<<<<< HEAD
    path('update/', views.update, name="update"),
=======
    path('search/',views.search,name='search'),
    path('<int:magazine_id>/',views.magazine_detail, name='magazine_detail'),
>>>>>>> 727601f5c4c76b686d9458fa2fd34bd7ffe7e7e5
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)