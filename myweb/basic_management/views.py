#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-12-11 22:17:37

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import template
from django import forms
from django.forms import extras
from templates import basic_management
from basic_management import models
from django.views.generic.list import ListView
from django import template
from django.contrib.auth.decorators import login_required

import datetime


@login_required
def generic_list(request, model, table_name=''):
    objects = model.objects.all()
    table_name = table_name
    paginate_by = 10
    return render(request,
                  'basic_management/{}s_list.html'.format(model.__name__.lower()),
                  locals())


@login_required
def generic_detail(request, pk, model, table_name=''):
    object = model.objects.get(id=pk)
    table_name = table_name

    return render(request,
                  'basic_management/{}s_detail.html'.format(model.__name__.lower()),
                  locals())

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
    fields = '__all__'
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyInfoCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Company info'
        return context


class CompanyInfoUpdate(UpdateView):
    model = models.Company_Info
    fields = '__all__'
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyInfoUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Company info'
        return context


class CompanyInfoDelete(DeleteView):
    model = models.Company_Info
    fields = ['name']
    template_name = 'generic_confirm_delete.html'
    success_url = reverse_lazy('company-list')

    def get_context_data(self, **kwargs):
        context = super(CompanyInfoDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Company info'
        return context


def company_search(request):
    company_Info = models.Company_Info
    name = request.GET.get('name')
    if 'key' in request.GET and request.GET['key'] != '':
        key = request.GET.get('key')
        if key == '1':
            company_list = company_Info.objects.filter(name__contains=name)
        if key == '2':
            company_list = company_Info.objects.filter(
                person_in_charge__contains=name)
        if key == '3':
            company_list = company_Info.objects.filter(
                phonenumbe__contains=name)

        return render(request, 'basic_management/company_info_search.html', {'company_list': company_list})
# =======employee=======================================


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


class EmployeeInfoCreate(CreateView):
    model = models.Employee_Info
    fields = '__all__'
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeInfoCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Employee info create'
        return context


class EmployeeInfoUpdate(UpdateView):
    model = models.Employee_Info
    fields = '__all__'
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


# =======Client=======================================


class ClientInfoForm(forms.ModelForm):

    current = datetime.datetime.now()
    birthday = forms.DateField(
        widget=forms.extras.SelectDateWidget(
            years=range(current.year - 150, current.year + 1)
        )
    )

    class Meta:
        model = models.Client_Info
        fields = '__all__'


class ClientInfoCreate(CreateView):
    model = models.Client_Info
    template_name = 'generic_form.html'
    form_class = ClientInfoForm

    def get_context_data(self, **kwargs):
        context = super(ClientInfoCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Client info create'
        return context


class ClientInfoUpdate(ClientInfoCreate, UpdateView):

    def get_context_data(self, **kwargs):
        context = super(ClientInfoUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Client info update'
        return context


class ClientInfoDelete(DeleteView):
    model = models.Client_Info
    fields = ['name']
    success_url = reverse_lazy('client_info-list')

    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(ClientInfoDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Client info'
        return context

def Client_search(request):
    Client_Info = models.Client_Info
    name = request.GET.get('name')
    if 'key' in request.GET and request.GET['key'] != '':
        key = request.GET.get('key')
        if key == '1':
            client_list = Client_Info.objects.filter(name__contains=name)

        return render(request, 'basic_management/employee_info_search.html', {'client_info_list': client_list})

# =======Product=======================================


def product_search(request):
    Product_Info = models.Product_Information
    name = request.GET.get('name')
    if 'key' in request.GET and request.GET['key'] != '':
        key = request.GET.get('key')
        if key == '1':
            Product_list = Product_Info.objects.filter(name__contains=name)
        if key == '2':
            Product_list = Product_Info.objects.filter(
                height__contains=name)
        if key == '3':
            Product_list = Product_Info.objects.filter(
                weight__contains=name)
        if key == '4':
            Product_list = Product_Info.objects.filter(
                price__contains=name)
        if key == '5':
            Product_list = Product_Info.objects.filter(
                categories_id__name__contains=name)
        return render(request, 'basic_management/product_Informations_search.html', {'Product_list': Product_list})


class ProductInformationCreate(CreateView):
    model = models.Product_Information
    fields = '__all__'
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductInformationCreate,
                        self).get_context_data(**kwargs)
        context['table_name'] = 'Product information create'
        return context


class ProductInformationUpdate(UpdateView):
    model = models.Product_Information
    fields = '__all__'
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductInformationUpdate,
                        self).get_context_data(**kwargs)
        context['table_name'] = 'Product information update'
        return context


class ProductInformationDelete(DeleteView):
    model = models.Product_Information
    fields = ['name']
    success_url = reverse_lazy('product_information-list')

    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(ProductInformationDelete,
                        self).get_context_data(**kwargs)
        context['table_name'] = 'Product information info'
        return context

# =======Categories=======================================


def Categories_search(request):
    Categories_Info = models.Categorie
    name = request.GET.get('name')
    if 'key' in request.GET and request.GET['key'] != '':
        key = request.GET.get('key')
        if key == '1':
            Categories_list = Categories_Info.objects.filter(
                name__contains=name)

        return render(request, 'basic_management/Categories_search.html', {'Categories_list': Categories_list})


class CategoriesCreate(CreateView):
    model = models.Categorie
    fields = '__all__'
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriesCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Categorie create'
        return context


class CategoriesUpdate(UpdateView):
    model = models.Categorie
    fields = '__all__'
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriesUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Categorie update'
        return context


class CategorieDelete(DeleteView):
    model = models.Categorie
    fields = ['name']
    success_url = reverse_lazy('categories-list')

    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(CategorieDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Categorie'
        return context


def Manufacturer_search(request):
    Manufacturer_Info = models.Manufacturer_Information
    name = request.GET.get('name')
    if 'key' in request.GET and request.GET['key'] != '':
        key = request.GET.get('key')
        if key == '1':
            Manufacturer_list = Manufacturer_Info.objects.filter(
                name__contains=name)
        if key == '2':
            Manufacturer_list = Manufacturer_Info.objects.filter(
                phonenumber__contains=name)
        if key == '3':
            Manufacturer_list = Manufacturer_Info.objects.filter(
                person_in_charge__contains=name)
        if key == '4':
            Manufacturer_list = Manufacturer_Info.objects.filter(
                Total_capital__contains=name)
        return render(request, 'basic_management/Manufacturer_Informations_search.html', {'Manufacturer_list': Manufacturer_list})


class ManufacturerInformationCreate(CreateView):
    model = models.Manufacturer_Information
    fields = '__all__'
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(ManufacturerInformationCreate,
                        self).get_context_data(**kwargs)
        context['table_name'] = 'Manufacturer information create'
        return context


class ManufacturerInformationUpdate(UpdateView):
    model = models.Manufacturer_Information
    fields = '__all__'
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super(ManufacturerInformationUpdate,
                        self).get_context_data(**kwargs)
        context['table_name'] = 'Manufacturer information update'
        return context


class ManufacturerInformationDelete(DeleteView):
    model = models.Manufacturer_Information
    fields = ['name']
    success_url = reverse_lazy('manufacturer_information-list')

    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(ManufacturerInformationDelete,
                        self).get_context_data(**kwargs)
        context['table_name'] = 'Manufacturer information info'
        return context


def Client_search(request):
    client_Info = models.Client_Info
    name = request.GET.get('name')
    if 'key' in request.GET and request.GET['key'] != '':
        key = request.GET.get('key')
        if key == '1':
            client_list = client_Info.objects.filter(name__contains=name)
        if key == '2':
            client_list = client_Info.objects.filter(
                phonenumber__contains=name)

        return render(request, 'basic_management/client_info_list_search.html', {'client_list': client_list})
