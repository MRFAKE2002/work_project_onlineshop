from django.contrib import admin

from .models import Product, Comment, Categories
from jalali_date.admin import ModelAdminJalaliMixin

class CommentProductInline(admin.TabularInline):
    model = Comment
    fields = ['user', 'text', 'stars', 'active',]
    extra = 0

@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name', 'price','is_active']
    
    inlines = [
        CommentProductInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'stars', 'active']



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    
