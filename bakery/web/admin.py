from django.contrib import admin

# Register your models here.
from web.models import Product, Category, DietList, CustomerProfile

admin.site.site_header = 'J B RICHARDSON BAKERY'

admin.site.register(Product)
admin.site.register(Category)
# admin.site.register(DietList)
admin.site.register(CustomerProfile)