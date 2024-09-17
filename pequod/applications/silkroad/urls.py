from django.urls import path
from . import views
from .views import mgProductoView

app_name = "silkroad_app"

urlpatterns = [
    path('productos_tienda', mgProductoView.as_view(), name='store_products_view',),
    
    ]
   