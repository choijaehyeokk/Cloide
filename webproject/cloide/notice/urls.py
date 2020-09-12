from django.urls import path
from . import views

urlpatterns = [
    path('<int:notice_id>' , views.detail, name ='detail'),  
    path('create/', views.create , name='create'),
    path('notice/' , views.notice, name='notice'),
]