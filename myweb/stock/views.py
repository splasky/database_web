#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-08 20:12:23

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
import datetime

from stock import models


def stock_search(request):
    stock = models.Stock_Info
    name = request.GET.get('name')
    s_id = request.GET.get('id')

    stock_list = stock.objects.filter(
        product__name__contains=name).filter(id__contains=s_id)
    return render(request, 'stock/stock_infos_search.html', {'stock_list': stock_list})


class StockInfoCreate(PermissionRequiredMixin, CreateView):
    model = models.Stock_Info
    fields = "__all__"
    template_name = 'generic_form.html'
    permission_required = 'stock.add_stock_info'

    def get_context_data(self, **kwargs):
        context = super(StockInfoCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Stock info create'
        return context


class StockInfoUpdate(StockInfoCreate, UpdateView):

    permission_required = 'stock.change_stock_info'

    def get_context_data(self, **kwargs):
        context = super(StockInfoUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Stock info update'
        return context


class StockInfoDelete(PermissionRequiredMixin, DeleteView):
    model = models.Stock_Info
    fields = ['product']
    success_url = reverse_lazy('stock_info-list')
    permission_required = 'stock.delete_stock_info'
    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(StockInfoDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Stock info'
        return context
