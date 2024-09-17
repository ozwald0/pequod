from django.contrib import admin
#
from .models import User, user_level, user_type, user_status, user_shipment_adress, user_bill_adress, assigned_user
#status

# Register your models here.

admin.site.register(User)
admin.site.register(user_level)
admin.site.register(user_type)
admin.site.register(user_status)
admin.site.register(user_shipment_adress)
admin.site.register(user_bill_adress)
admin.site.register(assigned_user)
