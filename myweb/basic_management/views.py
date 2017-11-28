#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-25 13:05:03

from django.shortcuts import render, get_object_or_404
from django.views import generic
from basic_management.models import Company_Info
from basic_management.models import Employee_Info
from basic_management.models import Client_Info
from basic_management.models import Categorie
from basic_management.models import Product_Information
from basic_management.models import Manufacturer_Information

from django import template
from templates import basic_management


def basic_management(request):
    table_name = 'Company_Infos'
    company_infos = Company_Info.objects.all()
    return render(request, 'basic_management.html', locals())


class employeeListView(generic.ListView):
    model = Employee_Info
    template_name = 'basic_management/employee_info.html'
    context_object_name = 'employee'


# class employeeCreateView(generic.FormView,SingleObjectMixin):
#     model=Employee_Info
    








class CompanyInfoListView(generic.ListView):
    model = Company_Info
    context_object_name = 'CompanyInfoList'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CompanyInfoListView, self).get_context_data(**kwargs)
        context['table_name'] = 'Company Info'
        return context


class CompanyDetailView(generic.DetailView):
    model = Company_Info
    context_object_name = 'company_detail'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['table_name'] = 'Company Detail'
        return context

class ClientInfoListView(generic.ListView):
    model = Client_Info
    context_object_name = 'Client_Info'
    template_name='basic_management/client_Info_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ClientInfoListView, self).get_context_data(**kwargs)
        context['table_name'] = 'Client Info'
        return context