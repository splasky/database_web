#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-04 16:48:30

# from framework
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

# create by us
from sales_management import views
from sales_management import models
from utils.util import generic_list

urlpatterns = [
    url(r'order/create/$',
        login_required(views.order_create),
        name='order_info-create'),
    url(r'order/(?P<pk>\d+)/update/$',
        login_required(views.order_update),
        name='order_info-update'),
    url(r'order/(?P<pk>\d+)/delete/$',
        login_required(views.OrderDelete.as_view()),
        name='order_info-delete'),
    url(r'^order/$',
        login_required(generic_list),
        {'app': 'sales_management', 'model': models.Order_Info, 'table_name': 'Order_Info'},
        name='order_info-list'),
    # url(r'^order/search/$',
    #     login_required(views.employee_search),
    url(r'order_detail/(?P<pk>\d+)/delete/$',
        login_required(views.OrderDetailDelete.as_view()),
        name='order_detail-delete'),#     name='employee-search'),
    url(r'^create_order_ajax/$', views.order_form_submit, name='create_order-ajax'),
]

