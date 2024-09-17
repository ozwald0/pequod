from django.db import models
from applications.halberd.models import user_bill_adress, user_shipment_adress
from applications.vanguard.models import products
from applications.halberd.models import User

# Create your models here.

from model_utils.models import TimeStampedModel


class sale_status(TimeStampedModel):
    sale_status_name = models.CharField(max_length=200)
    sale_status_description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + "--" + self.sale_status_name


class payment_method(TimeStampedModel):
    payment_method_name = models.CharField(max_length=200)
    payment_method_description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + "--" + self.payment_method_name


class sales(TimeStampedModel):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING, default=1) 
    shipment_adress = models.ForeignKey(user_shipment_adress, on_delete = models.DO_NOTHING)
    billing_details = models.ForeignKey(user_bill_adress, on_delete = models.DO_NOTHING)
    payment_method = models.ForeignKey(payment_method, on_delete = models.DO_NOTHING)
    status = models.ForeignKey(sale_status, on_delete = models.DO_NOTHING)
    total_amount = models.FloatField(max_length=200)

    def __str__(self):
        return str(self.id) + "--" + str(self.user)
    
    

class sale_details(TimeStampedModel):
    sale_details_sale_id = models.ForeignKey(sales, on_delete = models.DO_NOTHING)
    sale_details_producto_id = models.ForeignKey(products, on_delete = models.DO_NOTHING)
    sale_details_status = models.ForeignKey(sale_status, on_delete = models.DO_NOTHING)
    sale_details_product_price = models.FloatField()
    sale_details_product_amount = models.IntegerField()

    def __str__(self):
        return str(self.id) + "--" + str(self.sale_details_sale_id)

    
    
