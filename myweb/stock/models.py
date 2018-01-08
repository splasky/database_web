#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-08 19:26:34

from django.db import models
from django.urls import reverse
from basic_management.models import Product_Information


class Stock_Info(models.Model):

    product = models.ForeignKey(
        Product_Information,
        on_delete=models.CASCADE,
        verbose_name='商品'
    )
    quantity = models.IntegerField(verbose_name='數量')

    class Mate:
        db_table = 'Stock_Info'

    def get_absolute_url(self):
        return reverse('stock_info-update', args=[str(self.id)])

    def __str__(self):
        return '庫存名稱:{}'.format(self.product)
