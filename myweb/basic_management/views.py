#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-28 20:12:09

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import template
from basic_management import models
from basic_management import forms


def basic_management(request):
    table_name = 'Company_Infos'
    company_infos = models.Company_Info.objects.all()
    return render(request, 'basic_management.html', locals())


class EmployeeView(ListView):
    model = models.Employee_Info
    template_name = 'employee_info.html'
    context_object_name = 'employee'


class CompanyInfoCreate(CreateView):
    model = models.Company_Info
    fields = ['name', 'address', 'phonenumber',
              'EIN', 'person_in_charge', 'NUM_employee',
              'email', 'introduction']


class CompanyInfoUpdate(UpdateView):
    model = models.Company_Info
    fields = ['name', 'address', 'phonenumber',
              'EIN', 'person_in_charge', 'NUM_employee',
              'email', 'introduction']


class CompanyInfoDelete(DeleteView):
    model = models.Company_Info
    fields = ['name']
    success_url = reverse_lazy('company-list')


class CompanyInfoListView(generic.ListView):
    model = models.Company_Info
    context_object_name = 'CompanyInfoList'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CompanyInfoListView, self).get_context_data(**kwargs)
        context['table_name'] = 'Company Info'
        return context


class CompanyDetailView(generic.DetailView):
    model = models.Company_Info
    context_object_name = 'company_detail'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['table_name'] = 'Company Detail'
        return context
