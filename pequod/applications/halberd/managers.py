from django.db import models
#
from django.contrib.auth.models import BaseUserManager
from django.db.models import Q, F
#

class Usermanager(BaseUserManager, models.Manager):

    def _create_user(self, email, names, lastname, lastname2, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            email=email,
            names=names,
            lastname=lastname,
            lastname2=lastname2,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_user(self, email, names, lastname, lastname2, password=None, **extra_fields):
        return self._create_user(email, names, lastname, lastname2, password, False, False, True, **extra_fields)


    def create_superuser(self, email, names, lastname, lastname2, password=None, **extra_fields):
        return self._create_user(email, names, lastname, lastname2, password, True, True, True, **extra_fields)
    

    def search_users(self, kword, order):
        search = self.filter(
           Q(names__icontains=kword) | Q(email__icontains=kword) 
        )
        if order == 'id':
            return search.order_by('id')
        elif order == 'email':
            return search.order_by('email')
        elif order == 'names':
            return search.order_by('names')
        elif order == 'status':
            return search.order_by('status')
        elif order == 'type':
            return search.order_by('user_type')
        else:
            return search.order_by('-created')
        


class userLevelManager(models.Manager):

    def search_user_level(self, kword, order):
        search = self.filter(
           user_level_name__icontains=kword
        )
        if order == 'id':
            return search.order_by('id')
        elif order == 'name':
            return search.order_by('user_level_name')
        elif order == 'description':
            return search.order_by('user_level_description')
        elif order == 'number':
            return search.order_by('user_level_assigned_number')
        elif order == 'letter':
            return search.order_by('user_level_assigned_letter')
        else:
            return search.order_by('-created')
        

class userstatusManager(models.Manager):

    def search_user_status(self, kword, order):
        search = self.filter(
           user_status_name__icontains=kword
        )
        if order == 'id':
            return search.order_by('id')
        elif order == 'name':
            return search.order_by('user_status_name')
        elif order == 'description':
            return search.order_by('user_status_description')
        elif order == 'letter':
            return search.order_by('user_status_assigned_letter')
        else:
            return search.order_by('-created')
        

class userTypeManager(models.Manager):

    def search_user_type(self, kword, order):
        search = self.filter(
           user_type_name__icontains=kword
        )
        if order == 'id':
            return search.order_by('id')
        elif order == 'name':
            return search.order_by('user_type_name')
        elif order == 'description':
            return search.order_by('user_type_description')
        elif order == 'letter':
            return search.order_by('user_type_short_name')
        else:
            return search.order_by('-created')