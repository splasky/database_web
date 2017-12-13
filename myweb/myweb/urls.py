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
from basic_management.views import CompanyInfoCreate, CompanyInfoUpdate
from basic_management.views import CompanyInfoDelete, CompanyInfoListView
from basic_management.views import CompanyDetailView, employee_search, Client_search

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^basic_management/', include('basic_management.urls')),
    url(r'^accounts/register/$', register, name='register'),
    url(r'^$', login_required(index), name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),

]

urlpatterns += [
    

]

urlpatterns += [
    url(r'company/create/$',
        login_required(CompanyInfoCreate.as_view()),
        name='company-create'),
    url(r'company/(?P<pk>\d+)/update/$',
        login_required(CompanyInfoUpdate.as_view()),
        name='company-update'),
    url(r'company/(?P<pk>\d+)/delete/$',
        login_required(CompanyInfoDelete.as_view()),
        name='company-delete'),
    url(r'^company/$',
        login_required(CompanyInfoListView.as_view()),
        name='company-list'),
    url(r'^company/(?P<pk>\d+)$',
        login_required(CompanyDetailView.as_view()),
        name='company-detail'),


]
