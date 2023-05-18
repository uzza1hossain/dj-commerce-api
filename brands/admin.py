# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'description',
        'assets',
        'created_at',
        'updated_at',
    )
    list_filter = ('assets', 'created_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'created_at'
