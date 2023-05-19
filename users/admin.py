# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import CustomUser
from .models import SellerProfile
from .models import UserProfile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'is_seller',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'is_seller',
    )
    raw_id_fields = ('groups', 'user_permissions')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_picture')
    list_filter = ('user',)


@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_picture')
    list_filter = ('user',)
