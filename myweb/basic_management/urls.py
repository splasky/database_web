#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-12-15 15:00:33

"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see: 2017-12-11 22:15:19
    https: 2017-12-11 22:15:19
Examples: 2017-12-11 22:15:19
Function views
    1. Add an import: 2017-12-11 22:15:19
    2. Add a URL to urlpatterns: 2017-12-11 22:15:19
Class-based views
    1. Add an import: 2017-12-11 22:15:19
    2. Add a URL to urlpatterns: 2017-12-11 22:15:19
Including another URLconf
    1. Import the include() function: 2017-12-11 22:15:19
    2. Add a URL to urlpatterns: 2017-12-11 22:15:19
"""

# from framework
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

# create by us
from basic_management import views
from basic_management import models

urlpatterns = [
    url(r'employee/create/$',
        login_required(views.EmployeeInfoCreate.as_view()),
        name='employee-create'),
    url(r'employee/(?P<pk>\d+)/update/$',
        login_required(views.EmployeeInfoUpdate.as_view()),
        name='employee-update'),
    url(r'employee/(?P<pk>\d+)/delete/$',
        login_required(views.EmployeeInfoDelete.as_view()),
        name='employee-delete'),
    url(r'^employee/$',
        login_required(views.generic_list),
        {'model': models.Employee_Info, 'table_name': 'Employee_Info'},
        name='employee-list'),
    url(r'^employee/search/$',
        login_required(views.employee_search),
        name='employee-search'),
    url(r'^employee/(?P<pk>\d+)$',
        login_required(views.generic_detail),
        {'model': models.Employee_Info, 'table_name': 'Employee_Info'},
        name='employee-detail'),
]

urlpatterns += [
    url(r'company/create/$',
        login_required(views.CompanyInfoCreate.as_view()),
        name='company-create'),
    url(r'company/(?P<pk>\d+)/update/$',
        login_required(views.CompanyInfoUpdate.as_view()),
        name='company-update'),
    url(r'company/(?P<pk>\d+)/delete/$',
        login_required(views.CompanyInfoDelete.as_view()),
        name='company-delete'),
    url(r'^company/$',
        login_required(views.generic_list), {'model': models.Company_Info,
                                             'table_name': 'Company info'},
        name='company-list'),
    url(r'^company/(?P<pk>\d+)$',
        login_required(views.CompanyDetailView.as_view()),
        name='company-detail'),
    url(r'^company/search/$',
        login_required(views.company_search),
        name='company-search'),
]

urlpatterns += [
    url(r'client_info/create/$',
        login_required(views.ClientInfoCreate.as_view()),
        name='client_info-create'),
    url(r'client_info/(?P<pk>\d+)/update/$',
        login_required(views.ClientInfoUpdate.as_view()),
        name='client_info-update'),
    url(r'client_info/(?P<pk>\d+)/delete/$',
        login_required(views.ClientInfoDelete.as_view()),
        name='client_info-delete'),
    url(r'^client_info/$',
        login_required(views.generic_list),
        {'model': models.Client_Info, 'table_name': 'Client_Info'},
        name='client_info-list'),
    url(r'^client_info/(?P<pk>\d+)$',
        login_required(views.generic_detail),
        {'model': models.Client_Info, 'table_name': 'Client_Info'},
        name='client_info-detail'),
    url(r'^client/search/$',
        login_required(views.Client_search),
        name='client-search'),
]

urlpatterns += [
    url(r'product_information/create/$',
        login_required(views.ProductInformationCreate.as_view()),
        name='product_information-create'),
    url(r'product_information/(?P<pk>\d+)/update/$',
        login_required(views.ProductInformationUpdate.as_view()),
        name='product_information-update'),
    url(r'product_information/(?P<pk>\d+)/delete/$',
        login_required(views.ProductInformationDelete.as_view()),
        name='product_information-delete'),
    url(r'^product_information/$',
        login_required(views.generic_list),
        {'model': models.Product_Information, 'table_name': 'Product information'},
        name='product_information-list'),
    url(r'^product_information/(?P<pk>\d+)$',
        login_required(views.generic_detail),
        {'model': models.Product_Information, 'table_name': 'Product information'},
        name='product_information-detail'),
    url(r'product_information/search/$',
        login_required(views.product_search),
        name='product_information-search'),
]

urlpatterns += [
    url(r'categories/create/$',
        login_required(views.CategoriesCreate.as_view()),
        name='categories-create'),
    url(r'categories/(?P<pk>\d+)/update/$',
        login_required(views.CategoriesUpdate.as_view()),
        name='categories-update'),
    url(r'categories/(?P<pk>\d+)/delete/$',
        login_required(views.CategorieDelete.as_view()),
        name='categories-delete'),
    url(r'^categories/$',
        login_required(views.generic_list),
        {'model': models.Categorie, 'table_name': 'Categories'},
        name='categories-list'),
    url(r'categories/search/$',
        login_required(views.Categories_search),
        name='categories-search'),
]

urlpatterns += [
    url(r'manufacturer_information/create/$',
        login_required(views.ManufacturerInformationCreate.as_view()),
        name='manufacturer_information-create'),
    url(r'manufacturer_information/(?P<pk>\d+)/update/$',
        login_required(views.ManufacturerInformationUpdate.as_view()),
        name='manufacturer_information-update'),
    url(r'manufacturer_information/(?P<pk>\d+)/delete/$',
        login_required(views.ManufacturerInformationDelete.as_view()),
        name='manufacturer_information-delete'),
    url(r'^manufacturer/$',
        login_required(views.generic_list),
        {'model': models.Manufacturer_Information,
            'table_name': 'Manufacturer information'},
        name='manufacturer_information-list'),
    url(r'^manufacturer_information/(?P<pk>\d+)$',
        login_required(views.generic_detail),
        {'model': models.Manufacturer_Information,
            'table_name': 'Manufacturer detail'},
        name='manufacturer_information-detail'),
    url(r'manufacturer_information/search/$',
        login_required(views.Manufacturer_search),
        name='manufacturer_information-search'),
]
