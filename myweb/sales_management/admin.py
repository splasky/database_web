#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-09 09:55:56

from django.contrib import admin
from sales_management.models import *


class Basic_Info_Admin(admin.ModelAdmin):
    list_display = ('id', 'date', 'client_id',)
    search_fields = ('id', 'date', 'client_id',)

    class Mate:
        abstract = True


class Sales_InfoAdmin(Basic_Info_Admin):
    pass


class Returns_InfoAdmin(Basic_Info_Admin):
    pass


class Order_InfoAdmin(Basic_Info_Admin):
    pass


class Order_DetailsAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product_id', 'price', 'remark']
    search_fields = ['order_id', 'product_id', 'num_of_product', 'price', 'remark']


class Sales_DetailsAdmin(admin.ModelAdmin):
    list_display = ['sales_id', 'product_id', 'price', 'remark']
    search_fields = ['sales_id', 'product_id', 'num_of_product', 'price', 'remark']


class Returns_DetailsAdmin(admin.ModelAdmin):
    list_display = ['returns_id', 'product_id', 'price', 'remark']
    search_fields = ['returns_id', 'product_id', 'num_of_product', 'price', 'remark']

#  admin.site.register(Sales_Info, Sales_InfoAdmin)
#  admin.site.register(Returns_Info, Returns_InfoAdmin)
#  admin.site.register(Order_Info, Order_InfoAdmin)
#  admin.site.register(Order_Detail, Order_DetailsAdmin)
#  admin.site.register(Sales_Detail, Sales_DetailsAdmin)
#  admin.site.register(Returns_Detail, Returns_DetailsAdmin)
