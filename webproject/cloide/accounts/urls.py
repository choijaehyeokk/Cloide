from django.urls import path, include
from . import views

urlpatterns =[
    path('signup/',views.signup, name="signup"),
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
    path('update/', views.update, name="update"),
    path('oauth/', views.oauth, name="oauth"),
    path('accounts/', include('allauth.urls')),
]