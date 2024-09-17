from django.db import models
#
#from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from model_utils.models import TimeStampedModel
from .managers import productsmanager, suppliersmanager, productcategorymanager, productstatusmanager, brandsmanager, supplierstatusmanager, supplierlevelmanager
#
#from .managers import Usermanager

# Create your models here.

class brands(TimeStampedModel):
    brand_name = models.CharField(max_length=200)
    brand_description = models.CharField(max_length=200)
    brand_logo = models.ImageField(blank=True, null=True)
    brand_slogan = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + "--" + self.brand_name
    
    objects = brandsmanager()



class suppliers_status(TimeStampedModel):
    supplier_status_name = models.CharField(max_length=200)
    supplier_status_description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + "--" + self.supplier_status_name
    

    objects = supplierstatusmanager()
    
    


class suppliers_levels(TimeStampedModel):
    supplier_level_name = models.CharField(max_length=200)
    supplier_level_description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + "--" + self.supplier_level_name
    
    objects = supplierlevelmanager()


class suppliers(TimeStampedModel):
    supplier_name = models.CharField(max_length=200)
    supplier_description = models.CharField(max_length=200)
    supplier_brand = models.ManyToManyField(brands)
    supplier_level = models.ForeignKey(suppliers_levels, on_delete = models.DO_NOTHING)
    supplier_status = models.ForeignKey(suppliers_status, on_delete = models.DO_NOTHING)
    specialty = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + "--" + self.supplier_name

    objects = suppliersmanager()

#class product_types(TimeStampedModel):
#    product_type_name = models.CharField(max_length=200)
#    product_type_description = models.CharField(max_length=200)



class supplier_warehouses(TimeStampedModel):
    supplier_warehouse_name = models.CharField(max_length=200)
    supplier_warehouse_description = models.CharField(max_length=200)
    supplier_warehouse_adress = models.CharField(max_length=200)
    supplier_warehouse_state = models.CharField(max_length=200)
    supplier_warehouse_city = models.CharField(max_length=200)
    supplier_warehouse_supplier = models.ForeignKey(suppliers, on_delete = models.DO_NOTHING, default=1)
    #supplier_warehouse_status = models.CharField(max_length=200)
    #supplier_warehouse_type = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + "--" + self.supplier_warehouse_name


class product_categories(TimeStampedModel):
    product_category_name = models.CharField(max_length=200)
    product_category_description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + "--" + self.product_category_name
    
    objects = productcategorymanager()


class product_status(TimeStampedModel):
    product_status_name = models.CharField(max_length=200)
    product_status_description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + "--" + self.product_status_name
    
    objects = productstatusmanager()


class product_images(TimeStampedModel):
    product_image_name = models.CharField(max_length=200)
    product_image_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + "--" + self.product_image_name


#class producto_images(TimeStampedModel):
#    name = models.CharField(max_length=200)
#    description = models.CharField(max_length=200)


class products(TimeStampedModel):
    part_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.DecimalField('precio compra', max_digits=7, decimal_places=2)
    description = models.CharField(max_length=200)
    brand = models.ForeignKey(brands, on_delete = models.DO_NOTHING)
    model = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    supplier = models.ManyToManyField(suppliers)
    category = models.ForeignKey(product_categories, on_delete = models.DO_NOTHING, default=1)
    google_title = models.CharField(max_length=200)
    specs = models.TextField()
    sku = models.CharField(max_length=200)
    #product_type = models.ManyToManyField(suppliers)
    #product_line = models.CharField(max_length=200)
    product_status = models.ForeignKey(product_status, on_delete = models.DO_NOTHING)
    #product_images = models.ForeignKey(product_images, on_delete = models.DO_NOTHING)
    main_image = models.ImageField(upload_to='vanguard',blank=True, null=True)
    thumbnail = models.ImageField(upload_to='vanguard',blank=True, null=True)
    #tags = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    weight = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    deep = models.FloatField()

    def __str__(self):
        return self.category.product_category_name + "--" +  str(self.id) + "--" + self.name + "--" + self.part_number 
    
    objects = productsmanager()


#class cupon(TimeStampedModel):
#    name = models.CharField(max_length=200)
#    description = models.CharField(max_length=200)

#class tags(TimeStampedModel):
#    name = models.CharField(max_length=200)
#    description = models.CharField(max_length=200)


    


    
