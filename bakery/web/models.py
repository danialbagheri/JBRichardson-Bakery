# -*- coding: utf-8 -*-
# Create your models here.
from django.db import models
from django.db.models.signals import post_save
import datetime
from django.contrib.auth.models import User, Group


class CustomerProfile(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200, default='', blank=True)
    email_address = models.EmailField(max_length=500, default='', blank=True)
    phone = models.BigIntegerField(default=0, blank=True)
    addressline1 = models.CharField(max_length=200, default='', blank=True)
    addressline2 = models.CharField(max_length=200, default='', blank=True)
    postcode = models.CharField(max_length=10, default='', blank=True)
    account_created_date = models.DateTimeField(auto_now_add=True, blank=True)
    products = models.ManyToManyField('Product', default='')

    # TODO: Delivery address and invoicing address should be seprated
    def __str__(self):
        return self.customer_name


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    # parent = models.ForeignKey(
    #     'self',
    #     blank=True,
    #     null=True,
    #     related_name='child',
    #     on_delete=models.CASCADE)
    # slug = models.SlugField(default='')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return "%s" % (self.category_name)


class DietList(models.Model):
    diet_type = models.CharField(max_length=100)


class Product(models.Model):
    item_code = models.PositiveIntegerField(default=1)
    group_categories = models.ManyToManyField(Category, default='')
    # TODO: if product is a bread, we should ask if it is it needs to be sliced.
    product_name = models.CharField(max_length=200, default='')
    price = models.FloatField(
        default=1.0,
        blank=True,
    )
    sale_price = models.FloatField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    allergen = models.CharField(max_length=900, default='None', blank=True)
    # diet_list = models.ManyToManyField(
    # DietList, related_name='product', default='')
    weight = models.FloatField(default=1.0, blank=True)
    product_details = models.TextField(blank=True)
    ingredients = models.CharField(max_length=900, default='', blank=True)
    unique_product = models.BooleanField(default=False)

    class Meta:
        ordering = ['item_code']

    # TODO: Audit: we need to keep the record of where the item is sold to
    def __str__(self):
        return "%s - %s - %s" % (self.item_code, self.product_name, self.price)


# class Order (models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     po_number = models.CharField(max_length=40)
#     delivery_date = models.DateField(blank=False, default=datetime.date.today() + datetime.timedelta(days=1))
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     # payment_option = models.CharField(max_length=50)
#     order_status = models.CharField(max_length=50, default="PLACED")
#     quantity = models.IntegerField()
