#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-24 14:17:08

from django.shortcuts import render
from basic_management.models import Company_Info
from basic_management.models import Employee_Info
from basic_management.models import Client_Info
from basic_management.models import Categorie
from basic_management.models import Product_Information
from basic_management.models import Manufacturer_Information


def basic_management(request):
    table_name = 'Company_Infos'
    company_infos = Company_Info.objects.all()
    return render(request, 'basic_management.html', locals())
