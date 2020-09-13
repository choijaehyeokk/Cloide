"""cloide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
urlpatterns = [
    path('',views.firstpage, name='firstpage'),
    path('mage/', views.mage, name ='mage'),
    path('mage/mten', views.mten, name ='mten'),
    #path('',views.mstyle, name='mstyle'),
    path('mstyle/', views.mstyle, name = 'mstyle'),
    path('wstyle/', views.wstyle, name = 'wstyle'),
    
    path('mstyle/mage/', views.mage, name ='mage'),
    path('mstyle/mage/mten', views.mten, name ='mten'),
    path('mstyle/mage/mtwenty', views.mtwenty, name ='mtwenty'),
    path('mstyle/mage/mthirty', views.mthirty, name ='mthirty'),
    path('mstyle/mage/mfourty', views.mfourty, name ='mfourty'),

    path('wstyle/wage/', views.wage, name ='wage'),
    path('wstyle/wage/wten', views.wten, name ='wten'),
    path('mstyle/mage/wtwenty', views.mtwenty, name ='wtwenty'),
    path('mstyle/mage/wthirty', views.mthirty, name ='wthirty'),
    path('mstyle/mage/wfourty', views.mfourty, name ='wfourty'),
    path('mstyle/mage/wfourty', views.mfourty, name ='wfourty'),
]
