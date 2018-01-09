#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-09 09:56:07

from django.contrib import admin

from stock.models import *


class Stock_Info_Admin(admin.ModelAdmin):
    list_display = ('product',)
    search_fields = ('id', 'product', 'quantity')


#  admin.site.register(Stock_Info, Stock_Info_Admin)
