from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from applications.vanguard.models import products
# Create your views here.

class shieldwall2(ListView):
    template_name = "shieldwall/index.html"


    def get_queryset(self):
        queryset = products.objects.search_productos_latest("Gigabyte", "Asus", "lenovo", "MSI", "procesador")
        return queryset 
    

class frontProductDetail(DetailView):
    template_name = "shieldwall/front_products_view.html"
    model = products

