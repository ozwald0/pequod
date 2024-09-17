from django.contrib import admin

# Register your models here.

from .models import sale_status, payment_method, sales, sale_details

admin.site.register(sale_status)
admin.site.register(payment_method)
admin.site.register(sales)
admin.site.register(sale_details)