from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Product

admin.site.register(Customer)
admin.site.register(Product)