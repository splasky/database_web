#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-26 22:42:00

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

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from myweb.views import index, register
from basic_management.views import CompanyInfoListView, CompanyDetailView, employeeView, ClientInfoListView


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', register, name='register'),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^employee/$', employeeView.as_view(), name='employee'),
    url(r'^company/$', CompanyInfoListView.as_view(), name='company-list'),
    url(r'^company/(?P<pk>\d+)$', CompanyDetailView.as_view(), name='company-detail'),
    url(r'^client/$', ClientInfoListView.as_view(), name='client-list'),

]
