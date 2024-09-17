from django.contrib import admin

# Register your models here.
from .models import supplier_warehouses, brands, suppliers_status, suppliers_levels, suppliers, product_categories, product_status, product_images, products


admin.site.register(supplier_warehouses)
admin.site.register(brands)
admin.site.register(suppliers_status)
admin.site.register(suppliers_levels)
admin.site.register(suppliers)
admin.site.register(product_categories)
admin.site.register(product_status)
admin.site.register(product_images)
admin.site.register(products)