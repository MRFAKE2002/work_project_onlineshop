from django.contrib import admin

from .models import Order, OrderItems

class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    fields = ['user', 'text', 'stars', 'active',]
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','is_active']
    
    inlines = [
        OrderItemsInline,
    ]


@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'stars', 'active']

