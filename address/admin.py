# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Country, State, Address


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'zipcode_regex')
    search_fields = ('name',)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'country')
    raw_id_fields = ('country',)
    search_fields = ('name',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'street_address',
        'apt',
        'city',
        'country',
        'state',
        'zip_code',
        'phone_number',
        'content_type',
        'object_id',
    )
    list_filter = ('country', 'state', 'content_type')
