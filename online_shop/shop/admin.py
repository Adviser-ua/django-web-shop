from django.contrib import admin

# Register your models here.
from .models import Product


# Модель товара
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
#     list_filter = ['available', 'created', 'updated']
#     list_editable = ['price', 'stock', 'available']
#     prepopulated_fields = {'slug': ('name', )}

# admin.site.register(Product, ProductAdmin)
admin.site.register(Product)
