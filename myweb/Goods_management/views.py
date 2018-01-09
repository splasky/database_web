#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-09 09:41:03

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
from django.views.generic.edit import FormView

from Goods_management.models import Master, Detail, Purchase_Info
from basic_management.models import Product_Information, Client_Info, Employee_Info, Manufacturer_Information


class MasterForm(forms.Form):
    T = 'Purchase'
    F = 'Out'
    Manufacturer = forms.ChoiceField(
        choices=[(i.id, i.name) for i in Manufacturer_Information.objects.order_by('name')])
    staff = forms.ChoiceField(
        choices=[(i.id, i.name) for i in Employee_Info.objects.order_by('name')])
    contact_person = forms.CharField(label='聯絡人', max_length=16)
    contact_person_phone = forms.IntegerField(label='聯絡人電話',)
    remarks = forms.CharField(label='備註', max_length=200)
    address = forms.CharField(label='地址', max_length=200)
    choice = ((T, '進貨'), (F, '退貨'))
    status = forms.ChoiceField(
        label='進退貨狀態', choices=choice, widget=forms.Select(), required=True)


class Master_create(FormView):
    form_class = MasterForm
    template_name = 'goods_management/Masters_create.html'
    success_url = 'goods/create/'
    model = Product_Information

    def form_valid(self, form):
        Master.objects.create(
            Manufacturer=Manufacturer_Information.objects.get(
                id=form.cleaned_data['Manufacturer']
            ),
            staff=Employee_Info.objects.get(
                id=form.cleaned_data['staff']
            ),
            date=datetime.datetime.now(),
            contact_person=form.cleaned_data['contact_person'],
            contact_person_phone=form.cleaned_data[
                'contact_person_phone'],
            remarks=form.cleaned_data['remarks'],
            address=form.cleaned_data['address'],
            status=form.cleaned_data['status'],

        )
        return self.render_to_response(self.get_context_data())

    # if request.method == 'POST':
    #     return_form = MasterForm(requset.POST)
    # if return_form.is_valid():
    #     Manufacturer = Manufacturer_Info.objects.get(
    #         Manufacturer=return_form.cleaned_data['Manufacturer'])
    #     staff = Employee_Info.objects.get(
    #         staff=return_form.cleaned_data['staff']
    #     )
    #     goods_info = Master(
    #         Manufacturer=Manufacturer,
    #         staff=staff,
    #         date=datetime.datetime.now(),
    #         contact_person=return_form.cleaned_data['contact_person'],
    #         contact_person_phone=return_form.cleaned_data[
    #             'contact_person_phone'],
    #         remarks=return_form.cleaned_data['remarks'],
    #         address=return_form.cleaned_data['address'],
    #         status=return_form.cleaned_data['status'],
    #     )
    #     goods_info.save()

    #     return HttpResponseRedirect(reverse_lazy('goods_info-list'))
    # else:

    # return render(request, 'Goods_management/Masters_create.html', locals())
