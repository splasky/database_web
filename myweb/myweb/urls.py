#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-12-05 20:23:16

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

from myweb.views import index, register
from django.contrib.auth.decorators import login_required
# create by us
from myweb.views import index, register
from basic_management.views import CompanyInfoCreate, CompanyInfoUpdate
from basic_management.views import CompanyInfoDelete, CompanyInfoListView,EmployeeListView
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
    url(r'^employee/$',
        login_required(EmployeeListView.as_view()),
        name='employee'),
    url(r'^employee_search/$',
        login_required(employee_search),
        name='employee-search'),
    url(r'^client/search/$',
        login_required(Client_search),
        name='client-search'),

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
