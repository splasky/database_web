#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-08 19:34:28

# from framework
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

# create by us
from stock import views
from stock import models
from utils.util import generic_list

urlpatterns = [
    url(r'stock/create/$',
        login_required(views.StockInfoCreate.as_view()),
        name='stock_info-create'),
    url(r'stock/(?P<pk>\d+)/update/$',
        login_required(views.StockInfoUpdate.as_view()),
        name='stock_info-update'),
    url(r'stock/(?P<pk>\d+)/delete/$',
        login_required(views.StockInfoDelete.as_view()),
        name='stock_info-delete'),
    url(r'^stock/$',
        login_required(generic_list),
        {'app': 'stock', 'model': models.Stock_Info, 'table_name': 'Stock info'},
        name='stock_info-list'),
    # url(r'^order/search/$',
    #     login_required(views.employee_search),
]
