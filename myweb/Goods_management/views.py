#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-05 14:21:55

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from django.forms import extras
from django.http import JsonResponse, HttpResponseRedirect
import datetime
import random
from django.views.generic.list import ListView
from Goods_management.models import Master, Detail, Purchase_Info
from basic_management.models import Product_Information, Client_Info, Employee_Info


class MasterForm(forms.Form):
    T = 'Purchase'
    F = 'Out'
    Manufacturer = forms.CharField(label='廠商', max_length=100)
    staff = forms.CharField(label='經辦人', max_length=10)
    contact_person = forms.CharField(label='聯絡人', max_length=16)
    contact_person_phone = forms.IntegerField(label='聯絡人電話',)
    remarks = forms.CharField(label='備註', max_length=200)
    address = forms.CharField(label='地址', max_length=200)
    choice = ((T, '進貨'), (F, '退貨'))
    status = forms.ChoiceField(label='進退貨狀態', choices=choice)




def Master_create(requset):

    if request.method == 'POST':
        return_form = MasterForm(requset.POST)
    if return_form.is_valid():
        Manufacturer = Manufacturer_Info.objects.get(
            Manufacturer=return_form.cleaned_data['Manufacturer'])
        staff = Employee_Info.objects.get(
            staff=return_form.cleaned_data['staff']
        )
        goods_info = Master(
            Manufacturer=Manufacturer,
            staff=staff,
            date=datetime.datetime.now(),
            contact_person=return_form.cleaned_data['contact_person'],
            contact_person_phone=return_form.cleaned_data[
                'contact_person_phone'],
            remarks=return_form.cleaned_data['remarks'],
            address=return_form.cleaned_data['address'],
            status=return_form.cleaned_data['status'],
        )
        goods_info.save()

        return HttpResponseRedirect(reverse_lazy('goods_info-list'))
    else:

        form = order_form()
        table_name = "Order create"
        product_list = Product_Information.objects.order_by('name')
        return render(request, 'sales_management/order_infos_create.html', locals())
