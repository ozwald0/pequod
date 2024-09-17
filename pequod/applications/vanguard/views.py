from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import products, suppliers, product_categories, product_status, brands, suppliers_status, suppliers_levels
from .forms import (formUpdateproduct, formNewProduct, formUpdateSupplier, formNewSupplier, formUpdateProductCategory, 
                    formNewProductCategory, formUpdateProductStatus, formNewProductStatus, formUpdateBrand, formNewBrand,
                    formUpdateSupplierStatus, formNewSupplierStatus, formUpdateSupplierLevel, formNewSupplierLevel)




#--------------- products----------------------------------
class productsList(ListView):
    template_name = "vanguard/products_list.html"
    model = products

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        order = self.request.GET.get("order",'')
        queryset = products.objects.search_products(palabra_clave, order)
        return queryset


class productDetailView(DetailView):
    model = products
    template_name = "vanguard/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(productDetailView, self).get_context_data(**kwargs)
        context['ejemplo'] = "variable de ejemplo"
        return context


class productUpdate(UpdateView):
    template_name = "vanguard/product_update.html"
    model = products
    form_class = formUpdateproduct
    success_url = reverse_lazy('vanguard_app:products_list')


class newProductView(CreateView):
    model = products
    template_name = "vanguard/new_product.html"
    form_class = formNewProduct
    success_url = reverse_lazy('vanguard_app:products_list')


#-----------------suppliers-------------------------------------------
class supplierList(ListView):
    template_name = "vanguard/supplier_list.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        order = self.request.GET.get("order",'')
        queryset = suppliers.objects.search_suppliers(palabra_clave, order)
        return queryset


class supplierDetailView(DetailView):
    model = suppliers
    template_name = "vanguard/supplier_detail.html"


class supplierUpdateView(UpdateView):
    template_name = "vanguard/supplier_update.html"
    model = suppliers
    form_class = formUpdateSupplier
    success_url = reverse_lazy('vanguard_app:suppliers_list')


class newsupplier(CreateView):
    model = suppliers
    template_name = "vanguard/new_supplier.html"
    form_class = formNewSupplier
    success_url = reverse_lazy('vanguard_app:suppliers_list')



#------------------- product category-----------------------------------

class productCategoryList(ListView):
    template_name = "vanguard/product_category_list.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        order = self.request.GET.get("order",'')
        queryset = product_categories.objects.search_product_category(palabra_clave, order)
        return queryset



class productCategoryUpdateView(UpdateView):
    template_name = "vanguard/product_category_update.html"
    model = product_categories
    form_class = formUpdateProductCategory
    success_url = reverse_lazy('vanguard_app:product_category_list')


class newProductCategory(CreateView):
    model = product_categories
    template_name = "vanguard/new_product_category.html"
    form_class = formNewProductCategory
    success_url = reverse_lazy('vanguard_app:product_category_list')


#-------------------product status-----------------------------------

class productStatusList(ListView):
    template_name = "vanguard/product_status_list.html"
    model = product_status

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        order = self.request.GET.get("order",'')
        queryset = product_status.objects.search_product_status(palabra_clave, order)
        return queryset


class productStatusUpdate(UpdateView):
    template_name = "vanguard/product_status_update.html"
    model = product_status
    form_class = formUpdateProductStatus
    success_url = reverse_lazy('vanguard_app:product_status_list')


class newProductStatus(CreateView):
    model = product_status
    template_name = "vanguard/new_product_status.html"
    form_class = formNewProductStatus
    success_url = reverse_lazy('vanguard_app:product_status_list')

    
#-------------------brands-----------------------------------

class brandsList(ListView):
    template_name = "vanguard/brands_list.html"
    model = brands
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        order = self.request.GET.get("order",'')
        queryset = brands.objects.search_brands(palabra_clave, order)
        return queryset


class brandDetail(DetailView):
    model = brands
    template_name = "vanguard/brand_detail.html"



class productUpdateView(UpdateView):
    template_name = "vanguard/brand_update.html"
    model = brands
    form_class = formUpdateBrand
    success_url = reverse_lazy('vanguard_app:brands_list')


class newBrand(CreateView):
    model = brands
    template_name = "vanguard/new_brand.html"
    form_class = formNewBrand
    success_url = reverse_lazy('vanguard_app:brands_list')


#-------------------------------supplier status----------------------------------------

class supplierStatusList(ListView):
    template_name = "vanguard/supplier_status_list.html"
    model = suppliers_status
   
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        order = self.request.GET.get("order",'')
        queryset = suppliers_status.objects.search_supplier_status(palabra_clave, order)
        return queryset



class SupplierStatusUpdateView(UpdateView):
    template_name = "vanguard/supplier_status_update.html"
    model = suppliers_status
    form_class = formUpdateSupplierStatus
    success_url = reverse_lazy('vanguard_app:supplier_status_list')


class newSupplierStatus(CreateView):
    model = suppliers_status
    template_name = "vanguard/new_supplier_status.html"
    form_class = formNewSupplierStatus
    success_url = reverse_lazy('vanguard_app:supplier_status_list')

#--------------------supplier level -------------------------------------------------------


class supplierLevelList(ListView):
    template_name = "vanguard/suppliers_level_list.html"
    model = suppliers_levels
   
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        order = self.request.GET.get("order",'')
        queryset = suppliers_levels.objects.search_supplier_level(palabra_clave, order)
        return queryset



class SupplierLevelUpdateView(UpdateView):
    template_name = "vanguard/supplier_level_update.html"
    model = suppliers_levels
    form_class = formUpdateSupplierLevel
    success_url = reverse_lazy('vanguard_app:supplier_level_list')


class newSupplierLevel(CreateView):
    model = suppliers_levels
    template_name = "vanguard/new_supplier_level.html"
    form_class = formNewSupplierLevel
    success_url = reverse_lazy('vanguard_app:supplier_level_list')