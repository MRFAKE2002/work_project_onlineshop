from django.contrib import admin

from .models import Product, Comment, Category, Color, Size
from jalali_date.admin import ModelAdminJalaliMixin
from django.utils.translation import gettext_lazy as _


def make_active_True(modeladmin, request, queryset):
    queryset.update(is_active=True)
make_active_True.short_description = _("Make the product active.")


def make_status_True(modeladmin, request, queryset):
    queryset.update(status=True)
make_status_True.short_description = _("Make the product active.")

class CommentProductInline(admin.TabularInline):
    model = Comment
    
    fields = ['user', 'text', 'stars', 'active',]
    
    extra = 0

@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name', 'slug', 'categories_to_string', 'price', 'is_active', 'colors_to_string',]

    search_fields = ['name', 'slug']
    
    list_filter = ['is_active']

    ordering = ['is_active', 'name']
    
    actions = [make_active_True]
    
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
    
    actions = [make_status_True]
    
    prepopulated_fields = {'slug':['title']}


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'hex_code']

    search_fields = ['name']

    ordering = ['name']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['size_number']


