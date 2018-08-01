# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
import datetime
from django.contrib.auth.models import User
# from customer.models import CustomerProfile

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True,related_name='child', on_delete=models.CASCADE)
    slug = models.SlugField(default='')

    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = "Categories"
    def __str__(self):
        return "%s" %(self.category_name)
        

class DietList(models.Model):
    diet_type = models.CharField(max_length=100) 


class Product(models.Model):
    item_code = models.PositiveIntegerField(default=1)
    group_categories = models.ManyToManyField(Category,related_name='product', default='')
    # TODO: if product is a bread, we should ask if it is it needs to be sliced.
    product_name = models.CharField(max_length=200, default='')
    price = models.FloatField(default=1.0)
    sale_price = models.FloatField(default=None, null=True, blank=True)
    active = models.IntegerField(default='1')
    allergen = models.CharField(max_length=900,default='None',blank=True)
    diet_list = models.ManyToManyField(DietList, related_name='product', default='')
    weight = models.FloatField(default=1.0)
    product_details = models.TextField(blank=True)
    ingredients = models.CharField(max_length=900, default='',blank=True)
    unique_product = models.BooleanField(default=False)
    unique_product_for_customer = models.ForeignKey(User, on_delete=None, default='')
    class Meta:
        ordering = ['item_code']
    # TODO: Audit: we need to keep the record of where the item is sold to
    def __str__(self):
	    return "%s - %s - %s" %(self.item_code, self.product_name, self.price)



# class Order (models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     po_number = models.CharField(max_length=40)
#     delivery_date = models.DateField(blank=False, default=datetime.date.today() + datetime.timedelta(days=1))
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     # payment_option = models.CharField(max_length=50)
#     order_status = models.CharField(max_length=50, default="PLACED")
#     quantity = models.IntegerField()
