from django.contrib import admin
from basic_management.models import *
# Register your models here.


class Company_InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'person_in_charge',
                    'email', 'NUM_employee')
    search_fields = ('name', 'person_in_charge')


class Employee_InfoAdmin(admin.ModelAdmin):

    list_display = ('name', 'gender', 'comp_id')
    list_filter = ('gender',)
    search_fields = ('name', 'phonenumber')
# class Client_InfoAdmin(admin.ModelAdmin):

    # class CategoriesAdmin(admin.ModelAdmin):

    # class Product_InformationAdmin(admin.ModelAdmin):

    # class Manufacturer_InformationAdmin(admin.ModelAdmin):


admin.site.register(Company_Info, Company_InfoAdmin)
admin.site.register(Employee_Info, Employee_InfoAdmin)
# admin.site.register(Client_Info, Client_InfoAdmin)
