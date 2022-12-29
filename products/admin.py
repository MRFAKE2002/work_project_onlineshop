from django.contrib import admin

from .models import Product, Comment
from jalali_date.admin import ModelAdminJalaliMixin

class CommentProductInline(admin.TabularInline):
    model = Comment
    fields = ['user', 'product', 'stars', 'active',]
    extra = 1

@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active']
    
    inlines = [
        CommentProductInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'stars', 'active']
