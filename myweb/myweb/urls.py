#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-08 20:04:44

# -*- coding: utf-8 -*-

"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see: 2017-12-11 22:18:59
    https: 2017-12-11 22:18:59
Examples: 2017-12-11 22:18:59
Function views
    1. Add an import: 2017-12-11 22:18:59
    2. Add a URL to urlpatterns: 2017-12-11 22:18:59
Class-based views
    1. Add an import: 2017-12-11 22:18:59
    2. Add a URL to urlpatterns: 2017-12-11 22:18:59
Including another URLconf
    1. Import the include() function: 2017-12-11 22:18:59
    2. Add a URL to urlpatterns: 2017-12-11 22:18:59
"""

# from framework
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from myweb.views import index, register
from django.contrib.auth.decorators import login_required
# create by us
from myweb.views import index, register

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^basic_management/', include('basic_management.urls')),
    url(r'^sales_management/', include('sales_management.urls')),
    url(r'^stock/', include('stock.urls')),
    url(r'^accounts/register/$', register, name='register'),
    url(r'^$', login_required(index), name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
