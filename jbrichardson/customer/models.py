# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Group

class CustomerProfile(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200, default='', blank=True)
    email_address = models.EmailField(max_length=500, default='', blank=True)
    phone = models.BigIntegerField(default=0)
    addressline1 = models.CharField(max_length=200, default='', blank=True)
    addressline2 = models.CharField(max_length=200, default='', blank=True)
    postcode = models.CharField(max_length=10, default='',blank=True)
    account_created_date = models.DateTimeField(auto_now_add=True, blank=True)

    # TODO: Delivery address and invoicing address should be seprated
    def __str__(self):
        return self.customer_name

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)

ORDER_CHOICE = {
    's':'Successful',
    'r':'Refunded',
    'p':'Pending',
    'c':'Canceled',
}


# class Order_history(models.Model):
#     def number():
#         no = Cliente.objects.count()
#         if no == None:
#             return 000200
#         else:
#             return no + 1
#     order_number = models.IntegerField(max_length=6, unique=True, default=number)
#     customer = models.ForeignKey(User, on_delete=None)
#     order_status = models.ChoiceField(ORDER_CHOICE, default='s')

#     def __str__(self):
#         return self.customer_name
