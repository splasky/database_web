#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-12-28 20:54:42

from django.db import models
from django.urls import reverse
from basic_management.models import Client_Info
from basic_management.models import Product_Information


class Order_Info(models.Model):

    client_id = models.ForeignKey(
        Client_Info, on_delete=models.CASCADE, verbose_name='客戶id')
    invoice_number = models.CharField(verbose_name='統一編號', max_length=10)
    date = models.DateTimeField(verbose_name='輸入日期')
    estimated_shipping_date = models.DateTimeField(verbose_name='預計出貨日期')
    delivery_address = models.CharField(verbose_name='送貨地址', max_length=200)
    total = models.DecimalField(
        max_digits=20, decimal_places=4, verbose_name='合計')

    class Mate:
        db_table = 'Order_Info'

    def get_absolute_url(self):
        return reverse('order_info-update', args=[str(self.id)])

    def __str__(self):
        return '訂貨單號:{}'.format(self.id)


class Sales_Info(models.Model):

    date = models.DateTimeField(verbose_name='日期')
    client_id = models.ForeignKey(
        Client_Info, on_delete=models.CASCADE, verbose_name='客戶')
    total = models.DecimalField(
        max_digits=20, decimal_places=4, verbose_name='合計')

    class Mate:
        db_table = 'Sales_Info'

    def __str__(self):
        return '出貨單號:{}'.format(self.id)


class Returns_Info(models.Model):

    RETURNS_TYPES = (('E', 'Exchange'), ('R', 'Return'))

    date = models.DateTimeField(verbose_name='日期')
    client_id = models.ForeignKey(
        Client_Info, on_delete=models.CASCADE, verbose_name='會員編號')
    returns_reason = models.TextField(verbose_name='退貨原因', max_length=500)
    returns_type = models.CharField(
        max_length=2, choices=RETURNS_TYPES, default='E', verbose_name='退/換貨')
    total = models.IntegerField(verbose_name='合計')

    class Mate:
        db_table = 'Returns_Info'

    def get_absolute_url(self):
        return reverse('Returns_Info-detail', args=[str(self.id)])

    def __str__(self):
        return '退貨單號:{}'.format(self.id)


class Details_base(models.Model):

    product_id = models.ForeignKey(
        Product_Information, on_delete=models.CASCADE, verbose_name='商品id')
    price = models.IntegerField(verbose_name='售價')
    num_of_product = models.IntegerField(verbose_name='數量')
    subtotal = models.IntegerField(verbose_name='小計')
    remark = models.TextField(verbose_name='備註')

    class Mate:
        abstract = True
        ordering = ['id']


class Order_Detail(Details_base):
    order_id = models.ForeignKey(
        Order_Info, on_delete=models.CASCADE, verbose_name='訂貨單號')

    class Mate:
        db_table = 'Order_Details'

class Sales_Detail(Details_base):

    sales_id = models.ForeignKey(
        Sales_Info, on_delete=models.CASCADE, verbose_name='出貨單號')

    class Mate:
        db_table = 'Sales_Details'


class Returns_Detail(Details_base):

    returns_id = models.ForeignKey(
        Returns_Info, on_delete=models.CASCADE, verbose_name='退貨單號')

    class Mate:
        db_table = 'Returns_Details'
