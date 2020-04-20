from django.contrib import admin

# Register your models here.

from .models import Customer, Order, Agent

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Agent)