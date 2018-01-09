#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-04 16:48:30

# from framework
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

# create by us
from Goods_management import views
from Goods_management import models
from utils.util import generic_list,generic_detail

urlpatterns = [
    url(r'goods/create/$',
        login_required(views.Master_create.as_view()),
        name='Master_info-create'),
    url(r'goods/$',
        login_required(generic_list),
        {'app': 'Goods_management', 'model': models.Master, 'table_name': 'Master_Info'},
        name='goods_info-list'),
    url(r'goods/search/$',
        login_required(generic_list),
        {'app': 'Goods_management', 'model': models.Master, 'table_name': 'Master_Info'},
        name='Master-search'),
    url(r'^goods/(?P<pk>\d+)$',
        login_required(generic_detail),
        {'app': 'Goods_management','model': models.Master, 'table_name': 'Master_Info'},
        name='master-detail'),
    # url(r'order/create/$',
    #     login_required(views.order_create),
    #     name='order_info-create'),
    
]

