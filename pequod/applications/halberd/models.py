from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from model_utils.models import TimeStampedModel
#
from .managers import Usermanager, userLevelManager, userstatusManager, userTypeManager

# Create your models here.



class user_level(TimeStampedModel):
    user_level_name = models.CharField(max_length=200)
    user_level_description = models.TextField(blank = True)
    user_level_assigned_number = models.CharField(max_length=2)
    user_level_assigned_letter = models.CharField(max_length=2)
    user_level_short_name = models.CharField(max_length=50)
    user_level_code_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + "" + self.user_level_name
    
    objects = userLevelManager()


class user_type(TimeStampedModel):
    user_type_name = models.CharField(max_length=200)
    user_type_description = models.TextField(blank = True)
    user_type_short_name = models.CharField(max_length=50)
    user_type_code_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + "--" + self.user_type_name
    
    objects = userTypeManager()


class user_status(TimeStampedModel):
    user_status_name = models.CharField(max_length=200)
    user_status_description = models.TextField(blank = True)
    user_status_assigned_letter = models.CharField(max_length=2)
    user_status_short_name = models.CharField(max_length=50)
    user_status_code_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + "--" + self.user_status_name
    
    objects = userstatusManager()


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    names = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200, blank=True)
    lastname2 = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=200, default='Mexico')
    city = models.CharField(max_length=200,blank=True)
    user_level = models.ForeignKey(user_level, on_delete = models.DO_NOTHING, default=1)
    user_type = models.ForeignKey(user_type, on_delete = models.DO_NOTHING, default=1)
    status = models.ForeignKey(user_status, on_delete = models.DO_NOTHING, default=1)
    credit = models.BooleanField(default=False)
    credit_limit = models.FloatField(default=0)
    debt = models.FloatField(default=0)
    validation_code = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    last_access = models.DateTimeField(auto_now = True)
    #avatar = models.ImageField()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['names','lastname','lastname2']

    objects = Usermanager()


class user_shipment_adress(TimeStampedModel):
    user_shipment_adress_user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    user_shipment_adress_name = models.CharField(max_length=200, blank = True)
    user_shipment_adress_company_name = models.CharField(max_length=200, blank = True)
    user_shipment_adress_street = models.CharField(max_length=50, blank = True)
    user_shipment_adress_int_number = models.CharField(max_length=7, blank = True)
    user_shipment_adress_ext_number = models.CharField(max_length=7, blank = True)
    user_shipment_adress_colony = models.CharField(max_length=50, blank = True)
    user_shipment_adress_postal_code = models.CharField(max_length=10, blank = True)
    user_shipment_adress_city = models.CharField(max_length=100, blank = True)
    user_shipment_adress_municipio = models.CharField(max_length=100, blank = True)
    user_shipment_adress_state = models.CharField(max_length=100, blank = True)
    user_shipment_adress_phone = models.CharField(max_length=100, blank = True)
    user_shipment_adress_email = models.EmailField(max_length=200, blank = True)
    user_shipment_adress_references = models.CharField(max_length=100, blank = True)

    def __str__(self):
        return str(self.id) + "--" + str(self.user_shipment_adress_user)


class user_bill_adress(TimeStampedModel):
    user_bill_adress_user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    user_bill_adress_rfc = models.CharField(max_length=20, blank = True)
    user_bill_adress_street = models.CharField(max_length=50, blank = True)
    user_bill_adress_int_number = models.CharField(max_length=200, blank = True)
    user_bill_adress_ext_number = models.CharField(max_length=200, blank = True)
    user_bill_adress_colony = models.CharField(max_length=200, blank = True)
    user_bill_adress_postal_code = models.CharField(max_length=200, blank = True)
    user_bill_adress_city = models.CharField(max_length=200, blank = True)
    user_bill_adress_municipio = models.CharField(max_length=200, blank = True)
    user_bill_adress_state = models.CharField(max_length=200, blank = True)
    user_bill_adress_email = models.EmailField(max_length=200, blank = True)

    def __str__(self):
        return str(self.id) + "--" + str(self.user_bill_adress_user)



class assigned_user(TimeStampedModel):
    assigned_user_user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    assigned_user_assigned_salesman_email = models.EmailField(max_length=200)
    assigned_user_unassigment_date = models.DateTimeField(max_length=50, blank = True)
    assigned_user_unassign_reason = models.CharField(max_length=200, blank = True)
    assigned_user_status = models.BooleanField(max_length=200, default=False)
    assigned_user_comments = models.TextField(blank = True)

    def __str__(self):
        return str(self.id) + "--" + str(self.assigned_user_user)
