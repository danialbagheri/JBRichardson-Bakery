# -*- coding: utf-8 -*-
from django.contrib import admin
from product.models import Product, Category, DietList
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(DietList)
