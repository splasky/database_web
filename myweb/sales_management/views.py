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

from sales_management.models import Order_Info, Order_Detail
from basic_management.models import Product_Information, Client_Info


def order_form_submit(request):
    print(len(request.POST))
    print(request.POST.getlist('product_name[]'))
    print(request.POST.getlist('price[]'))
    print(request.POST.getlist('amount[]'))
    print(request.POST.getlist('subtotal[]'))
    print(request.POST.getlist('remark[]'))
    #  b = list(map(int, request.POST.getlist('b[]')))

    is_ajax = False
    if request.is_ajax():
        is_ajax = True

    test = {'POST': 'POST',
            'array': [1, 2, 3, 4],
            'is_ajax': is_ajax,
            }
    return JsonResponse(test)


class order_form(forms.Form):
    current = datetime.datetime.now()

    client = forms.ChoiceField(
        choices=[(i.id, i.name) for i in Client_Info.objects.order_by('name')])

    estimated_shipping_date = forms.DateTimeField(
        label='預計出貨日期',
        widget=forms.extras.SelectDateWidget()
    )
    delivery_address = forms.CharField(label='送貨地址', max_length=200)
    total = forms.DecimalField(label='合計', max_digits=20, decimal_places=4)


def order_create(request):
    if request.method == 'POST':
        return_form = order_form(request.POST)
        if return_form.is_valid():
            client = Client_Info.objects.get(
                id=return_form.cleaned_data['client'])
            order_info = Order_Info(
                client_id=client,
                invoice_number=random.randrange(0, 1000000, 6),
                date=datetime.datetime.now(),
                estimated_shipping_date=return_form.cleaned_data['estimated_shipping_date'],
                delivery_address=return_form.cleaned_data['delivery_address'],
                total=return_form.cleaned_data['total']
            )
            order_info.save()
            len_details = len(request.POST.getlist('key[]'))

            for i in range(len_details):
                key = request.POST.getlist('key[]')[i]
                price = request.POST.getlist('price[]')[i]
                amount = request.POST.getlist('amount[]')[i]
                subtotal = request.POST.getlist('subtotal[]')[i]
                remark = request.POST.getlist('remark[]')[i]
                product = Product_Information.objects.get(id=key)
                order_detail = Order_Detail.objects.create(
                    product_id=product,
                    price=price,
                    num_of_product=amount,
                    subtotal=subtotal,
                    remark=remark,
                    order_id=order_info
                )

            return HttpResponseRedirect(reverse_lazy('order_info-list'))
    else:
        form = order_form()
        table_name = "Order create"
        product_list = Product_Information.objects.order_by('name')
        return render(request, 'sales_management/order_infos_create.html', locals())


def order_update(request, pk):
    pass


def order_delete(request, pk):
    pass


def order_info_detail(request, pk):
    pass
