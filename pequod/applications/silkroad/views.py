from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from applications.vanguard.models import products
from applications.halberd.models import User

# Create your views here.


class mgProductoView(ListView):
    model = products
    template_name = "silkroad/product_view.html"

