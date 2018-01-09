#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-09 10:02:06

from django.contrib import admin
from Goods_management.models import *


class MasterAdmin(admin.ModelAdmin):
    list_display = ('Manufacturer_Info', 'date', 'staff',)

    class Mate:
        abstract = True


admin.site.register(Master, MasterAdmin)
