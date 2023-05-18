# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Product
from .models import ProductAttribute
from .models import ProductAttributeThrough
from .models import ProductAttributeValue
from .models import ProductVariant
from .models import VariantAttributeThrough


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
        'owner',
        'category',
        'brand',
        'assets',
        'is_active',
        'retail_price',
        'store_price',
        'is_digital',
        'weight',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'owner',
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


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'stock')
    list_filter = ('product',)
    raw_id_fields = ('attributes',)


@admin.register(VariantAttributeThrough)
class VariantAttributeThroughAdmin(admin.ModelAdmin):
    list_display = ('id', 'variant', 'attribute_value')
    list_filter = ('variant', 'attribute_value')


@admin.register(ProductAttributeThrough)
class ProductAttributeThroughAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'attribute', 'value')
    list_filter = ('product', 'attribute', 'value')
