from django.urls import path

#from . import views
from .views import (productsList, productDetailView, productUpdate, newProductView, supplierList, supplierDetailView, 
                    supplierUpdateView, newsupplier, productCategoryList, productCategoryUpdateView,newProductCategory,
                    productStatusList, productStatusUpdate, newProductStatus, brandsList, brandDetail, productUpdateView,
                    newBrand, supplierStatusList, SupplierStatusUpdateView, newSupplierStatus, supplierLevelList, SupplierLevelUpdateView, newSupplierLevel,
                    )

app_name = "vanguard_app"

urlpatterns = [
    path('products_list/', productsList.as_view(), name='products_list',),
    path('product_detail/<pk>', productDetailView.as_view(), name='product_detail',),
    path('product_update/<pk>', productUpdate.as_view(), name='product_update',),
    path('new_product/', newProductView.as_view(), name='new_product',),
    path('suppliers_list/', supplierList.as_view(), name='suppliers_list',),
    path('supplier_detail/<pk>', supplierDetailView.as_view(), name='supplier_detail',),
    path('supplier_update/<pk>', supplierUpdateView.as_view(), name='supplier_update',),
    path('new_supplier/', newsupplier.as_view(), name='new_supplier',),
    path('product_category_list/', productCategoryList.as_view(), name='product_category_list',),
    path('product_category_update/<pk>', productCategoryUpdateView.as_view(), name='product_category_update',),
    path('new_product_category/', newProductCategory.as_view(), name='new_product_category',),
    path('product_status_list/', productStatusList.as_view(), name='product_status_list',),
    path('product_status_update/<pk>', productStatusUpdate.as_view(), name='product_status_update',),
    path('new_product_status/', newProductStatus.as_view(), name='new_product_status',),
    path('brands_list/', brandsList.as_view(), name='brands_list',),
    path('brand_detail/<pk>', brandDetail.as_view(), name='brand_detail',),
    path('brand_update/<pk>', productUpdateView.as_view(), name='brand_update',),
    path('new_brand/', newBrand.as_view(), name='new_brand',),
    path('supplier_status_list/', supplierStatusList.as_view(), name='supplier_status_list',),
    path('supplier_status_update/<pk>', SupplierStatusUpdateView.as_view(), name='supplier_status_update',),
    path('new_supplier_status/', newSupplierStatus.as_view(), name='new_supplier_status',),
    path('supplier_level_list/', supplierLevelList.as_view(), name='supplier_level_list',),
    path('supplier_level_update/<pk>', SupplierLevelUpdateView.as_view(), name='supplier_level_update',),
    path('new_supplier_level/', newSupplierLevel.as_view(), name='new_supplier_level',),


    ]

"""
    


    
"""
   