# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import AssetFile
from .models import MediaAsset


@admin.register(MediaAsset)
class MediaAssetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'owner',
        'created_at',
        'updated_at',
    )
    list_filter = ('owner', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(AssetFile)
class AssetFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'alt_text')
    raw_id_fields = ('media_asset',)
