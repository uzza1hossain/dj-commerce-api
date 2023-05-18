# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import ProductAttribute, ProductAttributeValue, Product, ProductAttributeThrough


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute', 'value', 'description')
    list_filter = ('attribute',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'sku',
        'description',
        'category',
        'brand',
        'assets',
        'stock',
        'is_active',
        'retail_price',
        'store_price',
        'is_digital',
        'weight',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'category',
        'brand',
        'assets',
        'is_active',
        'is_digital',
        'created_at',
        'updated_at',
    )
    raw_id_fields = ('attributes',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'created_at'


@admin.register(ProductAttributeThrough)
class ProductAttributeThroughAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'attribute', 'value')
    list_filter = ('product', 'attribute', 'value')
