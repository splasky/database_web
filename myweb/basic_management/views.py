#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-28 20:12:09

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import template
from templates import basic_management
from basic_management import models
from django.views.generic.list import ListView
from django import template


def basic_management(request):
    table_name = 'Company_Infos'
    company_infos = models.Company_Info.objects.all()
    return render(request, 'basic_management.html', locals())


class employeeListView(generic.ListView):
    model = models.Employee_Info
    employee_field = model._meta.get_fields()
    template_name = 'basic_management/employee_info.html'
    context_object_name = 'employee'


def search(request):
    Employee_Info = models.Employee_Info
    name = request.GET.get('name')
    if 'key' in request.GET and request.GET['key'] != '':
        key = request.GET.get('key')
        if key == '1':
            employee_list = Employee_Info.objects.filter(name__contains=name)
        if key == '2':
            employee_list = Employee_Info.objects.filter(
                comp_id__contains=name)
        if key == '3':
            employee_list = Employee_Info.objects.filter(user__contains=name)
        if key == '4':
            employee_list = Employee_Info.objects.filter(
                phonenumber__contains=name)

        return render(request, 'basic_management/employee_info_search.html', {'employee_list': employee_list})


# class searchview(generic.ListView):
#     model = Employee_Info
#     template_name = 'basic_management/employee_info_search.html'
#     context_object_name = 'employee_list'


#     def get_context_data(self, **kwargs):
#         context = super(searchview, self).get_context_data(**kwargs)
#         context['employee_list'] = Employee_Info.objects.filter(name=pk)
#         return context

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


class ClientInfoListView(generic.ListView):
    model = models.Client_Info
    context_object_name = 'Client_Info'
    template_name = 'basic_management/client_Info_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ClientInfoListView, self).get_context_data(**kwargs)
        context['table_name'] = 'Client Info'
        return context
