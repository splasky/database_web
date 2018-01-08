#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-08 18:42:40

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
    invoice_number = forms.CharField(label='統一編號', max_length=20)
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
                invoice_number=return_form.cleaned_data['invoice_number'],
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
            return render(request, 'sales_management/order_infos_create.html', locals())
    else:
        form = order_form()
        table_name = "Order create"
        product_list = Product_Information.objects.order_by('name')
        return render(request, 'sales_management/order_infos_create.html', locals())


def order_update(request, pk):
    if request.method == 'POST':
        return_form = order_form(request.POST)
        if return_form.is_valid():
            Order_Info.objects.filter(pk=pk).update(
                client_id=Client_Info.objects.get(
                    id=return_form.cleaned_data['client']),
                estimated_shipping_date=return_form.cleaned_data['estimated_shipping_date'],
                delivery_address=return_form.cleaned_data['delivery_address'],
                total=return_form.cleaned_data['total'],
                invoice_number=return_form.cleaned_data['invoice_number']
            )

            len_details = len(request.POST.getlist('key[]'))
            for i in range(len_details):
                key = request.POST.getlist('key[]')[i]
                price = request.POST.getlist('price[]')[i]
                amount = request.POST.getlist('amount[]')[i]
                subtotal = request.POST.getlist('subtotal[]')[i]
                remark = request.POST.getlist('remark[]')[i]
                detail_id = request.POST.getlist('id[]')[i]
                product = Product_Information.objects.get(id=key)
                order_detail = Order_Detail.objects.filter(pk=detail_id).update(
                    product_id=product,
                    price=price,
                    num_of_product=amount,
                    subtotal=subtotal,
                    remark=remark
                )

        return HttpResponseRedirect(reverse_lazy('order_info-list'))
    else:
        order_info = Order_Info.objects.get(id=pk)
        form = order_form(initial={
            'client': order_info.client_id,
            'estimated_shipping_date': order_info.estimated_shipping_date,
            'delivery_address': order_info.delivery_address,
            'total': order_info.total,
            'invoice_number': order_info.invoice_number
        })
        table_name = "Order update"
        product_list = Product_Information.objects.order_by('name')

        order_details = Order_Detail.objects.filter(order_id=pk)
        return render(request, 'sales_management/order_infos_update.html', locals())


class OrderDelete(PermissionRequiredMixin, DeleteView):
    model = Order_Info
    template_name = 'generic_confirm_delete.html'
    success_url = reverse_lazy('order_info-list')
    permission_required = 'sales_management.delete_order_info'

    def get_context_data(self, **kwargs):
        context = super(OrderDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Order info'
        return context


class OrderDetailDelete(PermissionRequiredMixin, DeleteView):
    model = Order_Detail
    template_name = 'generic_confirm_delete.html'
    permission_required = 'sales_management.delete_order_detail'

    def get_context_data(self, **kwargs):
        context = super(OrderDetailDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Order detail'
        return context

    def get_success_url(self):
        order = self.object.order_id
        return reverse_lazy('order_info-update', kwargs={'pk': order.id})
