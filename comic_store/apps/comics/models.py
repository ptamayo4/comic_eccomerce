from __future__ import unicode_literals
from django.db import models
from decimal import Decimal
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def admin_login(self, post_data):
        error_msgs = []
        if User.userManager.get(email=post_data['email']) and User.userManager.get(email=post_data['email']).admin_auth:
            stored_pw = User.userManager.get(email=post_data['email']).password
            if stored_pw == post_data['password']:
                return {"admin": User.userManager.get(email=post_data['email'])}
            else:
                error_msgs.append("Invalid Login")
                return {"errors":error_msgs}
        else:
            error_msgs.append("Invalid Login")
            return {"errors":error_msgs}

    def user_login(self, post_data):
        error_msgs = []
        if User.userManager.get(email=post_data['email']):
            stored_pw = User.userManager.get(email=post_data['email']).password
            if stored_pw == post_data['password']:
                return {"theuser": User.userManager.get(email=post_data['email'])}
            else:
                error_msgs.append("Invalid Login")
                return {"errors":error_msgs}
        else:
            error_msgs.append("Invalid Login")
            return {"errors":error_msgs}
#class OrderManager(models.Manager):
#    def create_order(self, post_data, user_id):
#        the_user = User.objects.get(id=user_id)
#
#    def add_to_order(self, post_data, user_id):

class User(models.Model):
    email       =   models.CharField(max_length=100, default=None)
    password    =   models.CharField(max_length=100, default=None)
    first_name  =   models.CharField(max_length=60)
    last_name   =   models.CharField(max_length=60)
    admin_auth  =   models.BooleanField(default=False)
    addr_street =   models.CharField(max_length=100)
    street_two  =   models.CharField(max_length=100)
    addr_city   =   models.CharField(max_length=100)
    addr_state  =   models.CharField(max_length=20)
    addr_zip    =   models.IntegerField()
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)
    userManager =   UserManager()

class Product(models.Model):
    name        =   models.CharField(max_length=60)
    description =   models.TextField(max_length=1000)
    image       =   models.CharField(max_length=100)
    price       =   models.DecimalField(max_digits=5,decimal_places=2)
    #category    =   models.CharField(max_length=60)
    quantity    =   models.IntegerField(default=0)
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)

class Category(models.Model):
    name        =   models.CharField(max_length=60)
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)
    products    =   models.ManyToManyField(Product, related_name='product_categories')

class Order(models.Model):
    products    =   models.ManyToManyField(Product, related_name="product_orders")
    user        =   models.ForeignKey(User, related_name="user_orders")
    # shipping address
    addr_street =   models.CharField(max_length=100)
    street_two  =   models.CharField(max_length=100)
    addr_city   =   models.CharField(max_length=100)
    addr_state  =   models.CharField(max_length=20)
    ####
    total       =   models.DecimalField(max_digits=5,decimal_places=2)
    status      =   models.IntegerField(default=0)
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)
