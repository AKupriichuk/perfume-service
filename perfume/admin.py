from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from perfume.models import (
    Perfume,
    Perfumer,
    Customer,
    Manufacturer)


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'price')
    list_filter = ('manufacturer',)
    search_fields = ('name',)


@admin.register(Perfumer)
class PerfumerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'experience_years')


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    list_display = ('username', 'email', 'favourite_scent_family')


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')