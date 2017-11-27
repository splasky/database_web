#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-26 22:47:35

from django.contrib import admin
from basic_management.models import *


class Company_InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'person_in_charge',
                    'email', 'NUM_employee')
    search_fields = ('name', 'person_in_charge')


class Employee_InfoAdmin(admin.ModelAdmin):

    list_display = ('name', 'gender', 'comp_id')
    list_filter = ('gender',)
    search_fields = ('name', 'phonenumber')


class Client_InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phonenumber', 'gender')


class CategorieAdmin(admin.ModelAdmin):

    list_display = ('Categorie_name',)


class Product_InformationAdmin(admin.ModelAdmin):

    list_display = ('Product_name', 'Hight', 'Weight', 'Categories_id')


class Manufacturer_InformationAdmin(admin.ModelAdmin):
    list_display = ('Uniform_numbers',)


admin.site.register(Company_Info, Company_InfoAdmin)
admin.site.register(Employee_Info, Employee_InfoAdmin)
admin.site.register(Client_Info, Client_InfoAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Product_Information, Product_InformationAdmin)
admin.site.register(Manufacturer_Information, Manufacturer_InformationAdmin)
