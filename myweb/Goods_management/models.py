#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from django.db import models
from django.urls import reverse
from basic_management.models import Manufacturer_Information, Employee_Info
from basic_management.models import Categorie


class Master(models.Model):
    # 廠商(名稱、地址、電話)
    Manufacturer_Info = models.ForeignKey(
        Manufacturer_Information,
        models.DO_NOTHING,
        verbose_name='廠商',)

    # 時間
    date = models.DateTimeField('進貨日期',)
    # 經辦人# 驗收人
    # Applicant_staff# Acceptance_staff
    staff = models.ForeignKey(
        Employee_Info,
        models.DO_NOTHING,
        verbose_name='處理人員',)

    contact_person = models.CharField('聯絡人', max_length=16)
    contact_person_phone = models.IntegerField('聯絡電話',)
    remarks = models.TextField('備註', max_length=200, blank=True, null=True)
    address = models.CharField('地址', max_length=200)


class Detail(models.Model):
    # 分類
    Categorie = models.ForeignKey(
        Categorie,
        models.DO_NOTHING,
        verbose_name='分類',)
    # 商品名稱
    goods_name = models.CharField('產品名稱', max_length=100)
    # 單位
    unit = models.CharField('單位', max_length=10)
    # 數量
    count = models.IntegerField('數量',)
    # 單價
    price = models.FloatField('單價',)
    # 金額
    amount = models.FloatField('金額',)
    # 被註
    remarks = models.TextField('備註', blank=True, null=True)
    # 總金額
    total_amount = models.FloatField('總金額',)


class Purchase_Info(models.Model):

    master = models.ForeignKey(
        Master,
        models.DO_NOTHING,
        verbose_name='單頭',
    )
    detail = models.ForeignKey(
        Detail,
        models.DO_NOTHING,
        verbose_name='單身',
    )
