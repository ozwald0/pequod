#
from django.urls import path
from . import views

app_name = "shieldwall_app"

urlpatterns = [
    path('', views.shieldwall2.as_view(), name='index',),
    path('detalle_producto/<pk>', views.frontProductDetail.as_view(), name='front_product_detail',),
    
    ]
   