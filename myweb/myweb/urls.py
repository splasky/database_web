#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-22 13:28:15

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
from myweb.views import index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', index, name='index'),
]
