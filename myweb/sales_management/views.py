#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-20 21:43:49

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
from django.forms import formset_factory


def order_search(request):

    name = request.GET.get('name')
    client = request.GET.get('client')
    invoice_number = request.GET.get('invoice_number')
    order_list = Order_Info.objects.filter(
        client_id__name__contains=client).filter(id__contains=name).filter(
        invoice_number__contains=invoice_number)
    return render(request,
                  'sales_management/order_infos_search.html',
                  {'order_list': order_list})


class order_details_form(forms.Form):

    product_id_id = forms.ModelChoiceField(label="商品名稱",
                                           queryset=Product_Information.objects.order_by(
                                               'name'),
                                           widget=forms.Select(attrs={'class': 'product'}))

    price = forms.IntegerField(label="售價", min_value=0,
                               initial=0,
                               widget=forms.NumberInput(
                                   attrs={'class': 'price'}))
    num_of_product = forms.IntegerField(label="數量", min_value=0,
                                        initial=0,
                                        widget=forms.NumberInput(
                                            attrs={'class': 'quantity'}))
    subtotal = forms.IntegerField(label="小計", min_value=0, initial=0,
                                  widget=forms.NumberInput(
                                      attrs={'class': 'subtotal'}))
    remark = forms.CharField(label="備註", required=False)


class order_detail_update_form(order_details_form):
    id = forms.CharField()


class order_form(forms.Form):
    current = datetime.datetime.now()

    client = forms.ChoiceField(
        choices=[(i.id, i.name) for i in Client_Info.objects.order_by('name')])

    estimated_shipping_date = forms.DateTimeField(
        label='預計出貨日期',
        widget=forms.extras.SelectDateWidget()
    )
    invoice_number = forms.CharField(label='統一編號', max_length=10)
    delivery_address = forms.CharField(label='送貨地址', max_length=200)
    total = forms.DecimalField(label='合計',
                               max_digits=20,
                               decimal_places=4,
                               initial=0)


def order_create(request):

    menu_item_formset = formset_factory(
        order_details_form,
        extra=2, min_num=1
    )

    form = order_form()
    table_name = "Order create"

    if request.method == 'POST':

        return_form = order_form(request.POST)
        order_formset = menu_item_formset(request.POST, request.FILES)

        if return_form.is_valid() and order_formset.is_valid():

            client = Client_Info.objects.get(
                id=return_form.cleaned_data['client'])
            order_info = Order_Info(
                client_id=client,
                invoice_number=return_form.cleaned_data['invoice_number'],
                date=datetime.datetime.now(),
                estimated_shipping_date=return_form.cleaned_data[
                    'estimated_shipping_date'],
                delivery_address=return_form.cleaned_data['delivery_address'],
                total=return_form.cleaned_data['total']
            )
            order_info.save()

            for form in order_formset:
                Order_Detail.objects.create(
                    product_id=form.cleaned_data['product_id_id'],
                    price=form.cleaned_data['price'],
                    num_of_product=form.cleaned_data['num_of_product'],
                    subtotal=form.cleaned_data['subtotal'],
                    remark=form.cleaned_data['remark'],
                    order_id=order_info
                )

        return HttpResponseRedirect(reverse_lazy('order_info-list'))

    return render(request,
                  'sales_management/order_infos_create.html',
                  locals())


def order_update(request, pk):

    table_name = "Order update"

    if request.method == 'POST':
        return_form = order_form(request.POST)
        formsets = formset_factory(
            order_detail_update_form
        )
        order_formset = formsets(request.POST, request.FILES)

        if return_form.is_valid():
            Order_Info.objects.filter(pk=pk).update(
                client_id=Client_Info.objects.get(
                    id=return_form.cleaned_data['client']),
                estimated_shipping_date=return_form.cleaned_data[
                    'estimated_shipping_date'],
                delivery_address=return_form.cleaned_data['delivery_address'],
                total=return_form.cleaned_data['total'],
                invoice_number=return_form.cleaned_data['invoice_number']
            )

        if order_formset.is_valid():
            for form in order_formset:
                if not form.cleaned_data:
                    break
                detail_id = form.cleaned_data.get('id')
                order_detail = Order_Detail.objects.filter(pk=detail_id).update(
                    product_id=form.cleaned_data['product_id_id'],
                    price=form.cleaned_data['price'],
                    num_of_product=form.cleaned_data['num_of_product'],
                    subtotal=form.cleaned_data['subtotal'],
                    remark=form.cleaned_data['remark']
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

        order_details = Order_Detail.objects.filter(order_id=pk).values()
        formsets = formset_factory(
            order_detail_update_form, min_num=1
        )
        menu_item_formset = formsets(initial=order_details)

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
