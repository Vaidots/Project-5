from django.contrib import admin
from .models import Product, Category, Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'rating', 'created_on')
    list_filter = ('rating', 'created_on')
    search_fields = ('name', 'product__name', 'body')
    readonly_fields = ('created_on',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)