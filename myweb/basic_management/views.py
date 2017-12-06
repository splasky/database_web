#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-12-06 15:21:53

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
from django.contrib.auth.decorators import login_required


@login_required
def generic_list(request, model, table_name=''):
    objects = model.objects.all()
    table_name = table_name
    paginate_by = 10
    return render(request,
                  '{}s_list.html'.format(model.__name__.lower()),
                  locals())


class employeeListView(generic.ListView):
    model = models.Employee_Info
    employee_field = model._meta.get_fields()
    template_name = 'basic_management/employee_info.html'
    context_object_name = 'employee'


def employee_search(request):
    Employee_Info = models.Employee_Info
    name = request.GET.get('name')
    if 'key' in request.GET and request.GET['key'] != '':
        key = request.GET.get('key')
        if key == '1':
            employee_list = Employee_Info.objects.filter(name__contains=name)
        if key == '2':
            employee_list = Employee_Info.objects.filter(
                comp_id__name__contains=name)
        if key == '3':
            employee_list = Employee_Info.objects.filter(
                user__username__contains=name)
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


class CompanyInfoListView(generic.ListView):
    model = models.Company_Info
    context_object_name = 'CompanyInfoList'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CompanyInfoListView, self).get_context_data(**kwargs)
        context['table_name'] = 'Company info'
        return context


class CompanyDetailView(generic.DetailView):
    model = models.Company_Info
    context_object_name = 'company_detail'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['table_name'] = 'Company detail'
        return context


class CompanyInfoCreate(CreateView):
    model = models.Company_Info
    fields = ['name', 'address', 'phonenumber',
              'EIN', 'person_in_charge', 'NUM_employee',
              'email', 'introduction']
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyInfoCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Company info'
        return context


class CompanyInfoUpdate(UpdateView):
    model = models.Company_Info
    fields = ['name', 'address', 'phonenumber',
              'EIN', 'person_in_charge', 'NUM_employee',
              'email', 'introduction']
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyInfoUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Company info'
        return context


class CompanyInfoDelete(DeleteView):
    model = models.Company_Info
    fields = ['name']
    success_url = reverse_lazy('company-list')

    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyInfoDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Company info'
        return context


class EmployeeInfoCreate(CreateView):
    model = models.Employee_Info
    fields = ['name', 'address', 'phonenumber',
              'email', 'phonenumber', 'EMP_gender',
              'gender', 'birthday', 'comp_id', 'user']
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeInfoCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Employee info create'
        return context


class EmployeeInfoUpdate(UpdateView):
    model = models.Employee_Info
    fields = ['name', 'address', 'phonenumber',
              'email', 'phonenumber', 'EMP_gender',
              'gender', 'birthday', 'comp_id', 'user']

    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeInfoUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Employee info update'
        return context


class EmployeeInfoDelete(DeleteView):
    model = models.Employee_Info
    fields = ['name']
    success_url = reverse_lazy('Employee-list')

    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeInfoDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Employee info'
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


class ClientInfoCreate(CreateView):
    model = models.Client_Info
    fields = ['name', 'address', 'phonenumber',
              'email', 'CLIENT_gender', 'gender',
              'birthday']
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(ClientInfoCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Employee info create'
        return context


class ClientInfoUpdate(UpdateView):
    model = models.Client_Info
    fields = ['name', 'address', 'phonenumber',
              'email', 'CLIENT_gender', 'gender',
              'birthday']
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(ClientInfoUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Client info update'
        return context


class ClientInfoDelete(DeleteView):
    model = models.Client_Info
    fields = ['name']
    success_url = reverse_lazy('Client-list')

    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(ClientInfoDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Employee info'
        return context


class ProductInformationCreate(CreateView):
    model = models.Product_Information
    fields = ['product_name', 'height', 'weight', 'price', 'categories_id']
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductInformationCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Product information create'
        return context


class ProductInformationUpdate(UpdateView):
    model = models.Product_Information
    fields = ['product_name', 'height', 'weight', 'price', 'categories_id']
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductInformationUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Product information update'
        return context


class ProductInformationDelete(DeleteView):
    model = models.Product_Information
    fields = ['product_name']
    success_url = reverse_lazy('product_information-list')

    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(ProductInformationDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Product information info'
        return context


class CategoriesCreate(CreateView):
    model = models.Categorie
    fields = ['Categorie_name']
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriesCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Categorie create'
        return context


class CategoriesUpdate(UpdateView):
    model = models.Categorie
    fields = ['Categorie_name']
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriesUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Categorie update'
        return context


class CategorieDelete(DeleteView):
    model = models.Categorie
    fields = ['Categorie_name']
    success_url = reverse_lazy('categorie-list')

    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(CategorieDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Categorie'
        return context


class ManufacturerInformationCreate(CreateView):
    model = models.Manufacturer_Information
    fields = ['name', 'address', 'phonenumber', 'EIN', 'person_in_charge',
              'NUM_employee', 'email', 'introduction', 'Total_capital']
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(ManufacturerInformationCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Manufacturer information create'
        return context


class ManufacturerInformationUpdate(UpdateView):
    model = models.Manufacturer_Information
    fields = ['name', 'address', 'phonenumber', 'EIN', 'person_in_charge',
              'NUM_employee', 'email', 'introduction', 'Total_capital']
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(ManufacturerInformationUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Manufacturer information update'
        return context


class ManufacturerInformationDelete(DeleteView):
    model = models.Manufacturer_Information
    fields = ['name']
    success_url = reverse_lazy('manufacturer_information-list')

    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(ManufacturerInformationDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Manufacturer information info'
        return context
