#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-12-06 17:02:02

"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
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
        login_required(views.employeeListView.as_view()),
        name='employee-list'),
    url(r'^employee_search/$',
        login_required(views.employee_search),
        name='employee_search'),
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
        login_required(views.CompanyInfoListView.as_view()),
        name='company-list'),
    url(r'^company/(?P<pk>\d+)$',
        login_required(views.CompanyDetailView.as_view()),
        name='company-detail'),
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
        login_required(views.ClientInfoListView.as_view()),
        name='client_info-list'),
    url(r'^client_info/(?P<pk>\d+)$',
        login_required(views.generic_detail),
        {'model': models.Client_Info, 'table_name': 'Client info'},
        name='client_info-detail'),
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
        {'model': models.Manufacturer_Information, 'table_name': 'Manufacturer information'},
        name='manufacturer_information-list'),
    url(r'^manufacturer_information/(?P<pk>\d+)$',
        login_required(views.generic_detail),
        {'model': models.Manufacturer_Information, 'table_name': 'Manufacturer detail'},
        name='manufacturer_information-detail'),
]
