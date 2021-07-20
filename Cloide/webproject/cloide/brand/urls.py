from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.brand, name='brand'),
    path('brand_detail/',views.brand_detail, name = 'brand_detail'),
    path('user_brand_add/',views.user_brand_add, name='user_brand_add'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)