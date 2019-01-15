from django.contrib import admin

# Register your models here.
from web.models import Product, Category, DietList, CustomerProfile, Order
from django.contrib.admin import AdminSite

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "tracking_number",
        "customer",
        "delivery_date",
        "po_number"
    )

admin.site.site_header = 'J B RICHARDSON BAKERY'

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(CustomerProfile)