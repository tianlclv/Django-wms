from django.contrib import admin

from .models import Luser, Order, Track, Product, Address


admin.site.register(Luser)
admin.site.register(Order)
admin.site.register(Track)
admin.site.register(Product)
admin.site.register(Address)
