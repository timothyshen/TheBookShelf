from django.contrib import admin
from .models import Billing_address, Order, OrderItem

# Register your models here.
admin.site.register(Billing_address)
admin.site.register(Order)
admin.site.register(OrderItem)
