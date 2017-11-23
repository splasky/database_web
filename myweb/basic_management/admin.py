#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-23 17:23:14

from django.contrib import admin
from basic_management.models import *

admin.site.register(Company_Info)
admin.site.register(Employee_Info)
admin.site.register(Client_Info)
admin.site.register(Categories)
admin.site.register(Product_Information)
admin.site.register(Manufacturer_Information)
