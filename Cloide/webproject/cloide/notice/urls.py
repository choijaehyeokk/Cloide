from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('<int:notice_id>' , views.detail, name ='detail'),  
    path('create/', views.create , name='create'),
    path('notice/' , views.notice, name='notice'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)