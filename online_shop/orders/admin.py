from django.contrib import admin
from .models import Order, OrderItem


class PropertyImageInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'price', 'quantity')


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline, ]


admin.site.register(Order, PropertyAdmin)
