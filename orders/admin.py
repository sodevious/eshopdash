from django.contrib import admin
from .models import Order

# 
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('item')

admin.site.register(Order)
