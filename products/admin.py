from django.contrib import admin

from .models import Product, Comment, Category
from jalali_date.admin import ModelAdminJalaliMixin

class CommentProductInline(admin.TabularInline):
    model = Comment
    
    fields = ['user', 'text', 'stars', 'active',]
    
    extra = 0

@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name', 'slug', 'categories_to_string', 'price', 'is_active']

    search_fields = ['name', 'slug']
    
    list_filter = ['is_active']

    ordering = ['is_active', 'name']
    
    inlines = [
        CommentProductInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'stars', 'active']

    search_fields = ['product', 'user']

    list_filter = ['active', 'product']

    ordering = ['product']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['position', 'title', 'status']
    
    list_filter = ['status']
    
    search_fields = ['title', 'slug']
    
    ordering = ['position']
    
    prepopulated_fields = {'slug':['title']}

