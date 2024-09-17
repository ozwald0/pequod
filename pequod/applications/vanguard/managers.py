from django.db import models
from django.db.models import Q, F
from itertools import chain


class productsmanager(models.Manager):

    def search_products(self, kword, order):
            search = self.filter(
            Q(part_number__icontains=kword) | Q(model__icontains=kword) | Q(name__icontains=kword) 
            )
            if order == 'id':
                return search.order_by('id')
            elif order == 'part':
                return search.order_by('part_number')
            elif order == 'name':
                return search.order_by('name')
            elif order == 'brand':
                return search.order_by('brand__brand_name')
            elif order == 'quantity':
                return search.order_by('quantity')
            else:
                return search.order_by('-created')
            
    
    def search_productos_latest(self, word1, word2, word3, word4, word5):
            
            search1 = self.filter(
            brand__brand_name__icontains=word1
            ).order_by('-created')[:4]
            search2 = self.filter(
            brand__brand_name__icontains=word2
            ).order_by('-created')[:4]
            search3 = self.filter(
            brand__brand_name__icontains=word3
            ).order_by('-created')[:4]
            search4 = self.filter(
            brand__brand_name__icontains=word4
            ).order_by('-created')[:4]
            search5 = self.filter(
            category__product_category_name__icontains=word5
            ).order_by('-created')[:4]
            search= list(chain(search1, search2, search3, search4, search5))
            #search = search1 + search2 + search3 + search4
            return search



class suppliersmanager(models.Manager):

    def search_suppliers(self, kword, order):
            search = self.filter(
            Q(supplier_name__icontains=kword) 
            )
            if order == 'id':
                return search.order_by('id')
            elif order == 'part':
                return search.order_by('supplier_name')
            elif order == 'name':
                return search.order_by('supplier_level__supplier_level_name')
            elif order == 'brand':
                return search.order_by('supplier_status__supplier_status_name')
            else:
                return search.order_by('-created')
            


class productcategorymanager(models.Manager):

    def search_product_category(self, kword, order):
            search = self.filter(
            Q(product_category_name__icontains=kword) 
            )
            if order == 'id':
                return search.order_by('id')
            elif order == 'part':
                return search.order_by('product_category_name')
            elif order == 'name':
                return search.order_by('product_category_description')
            else:
                return search.order_by('-created')
            

class productstatusmanager(models.Manager):

    def search_product_status(self, kword, order):
            search = self.filter(
            Q(product_status_name__icontains=kword) 
            )
            if order == 'id':
                return search.order_by('id')
            elif order == 'part':
                return search.order_by('product_status_name')
            elif order == 'name':
                return search.order_by('product_status_description')
            else:
                return search.order_by('-created')



class brandsmanager(models.Manager):

    def search_brands(self, kword, order):
            search = self.filter(
            Q(brand_name__icontains=kword) 
            )
            if order == 'id':
                return search.order_by('id')
            elif order == 'brand':
                return search.order_by('brand_name')
            elif order == 'description':
                return search.order_by('brand_description')
            elif order == 'slogan':
                return search.order_by('brand_slogan')
            else:
                return search.order_by('-created')
            

class supplierstatusmanager(models.Manager):

    def search_supplier_status(self, kword, order):
            search = self.filter(
            Q(supplier_status_name__icontains=kword) 
            )
            if order == 'id':
                return search.order_by('id')
            elif order == 'name':
                return search.order_by('supplier_status_name')
            elif order == 'description':
                return search.order_by('supplier_status_description')
            else:
                return search.order_by('-created')
            

class supplierlevelmanager(models.Manager):

    def search_supplier_level(self, kword, order):
            search = self.filter(
            Q(supplier_level_name__icontains=kword) 
            )
            if order == 'id':
                return search.order_by('id')
            elif order == 'name':
                return search.order_by('supplier_level_name')
            elif order == 'description':
                return search.order_by('supplier_level_description')
            else:
                return search.order_by('-created')
  

#class ProductsManager(models.Manager):

    #def search_product(self, kword, order): 
    #    #se hace el filtro con el kword que se manda desde el search
    #    consulta = self.filter(
    #        Q(name__icontains=kword) | Q(sku=kword)
    #    )
    #    #se verifica en que orden lo solicita el cliente
    #    if order == 'date':
    #        return consulta.order_by('created')
    #    elif order == 'name':
    #        return consulta.order_by('name')
    #    elif order == 'quantity':
    #        return consulta.order_by('quantity')
    #    else:
    #        return consulta.order_by('-created')
        