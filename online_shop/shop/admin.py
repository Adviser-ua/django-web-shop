from django.contrib import admin

# Register your models here.
from .models import Product, ProductImages


class PropertyImageInline(admin.TabularInline):
    model = ProductImages
    extra = 1


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline, ]


admin.site.register(Product, PropertyAdmin)
