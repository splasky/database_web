#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-17 20:09:23

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render
from django.forms import extras
from django.http import JsonResponse
from django import forms
# TODO::use generic detail
from django.views import generic
import datetime

from basic_management import models


def test(request):
    Employee_Info = models.Employee_Info
    employee_list = Employee_Info.objects.order_by('name')
    return render(request, 'basic_management/test.html', {'employee_list': employee_list})


@login_required
def generic_list(request, model, table_name=''):
    objects = model.objects.all()
    table_name = table_name
    paginate_by = 10
    return render(request,
                  'basic_management/{}s_list.html'.format(
                      model.__name__.lower()),
                  locals())


@login_required
def generic_detail(request, pk, model, table_name=''):
    object = model.objects.get(id=pk)
    table_name = table_name

    return render(request,
                  'basic_management/{}s_detail.html'.format(
                      model.__name__.lower()),
                  locals())

# =======Company=======================================


class CompanyDetailView(generic.DetailView):
    model = models.Company_Info
    context_object_name = 'company_detail'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['table_name'] = 'Company detail'
        return context


class CompanyInfoCreate(PermissionRequiredMixin, CreateView):
    model = models.Company_Info
    fields = '__all__'
    template_name = 'generic_form.html'
    permission_required = 'basic_management.add_company_info'

    def get_context_data(self, **kwargs):
        context = super(CompanyInfoCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Company info'
        return context


class CompanyInfoUpdate(PermissionRequiredMixin, UpdateView):
    model = models.Company_Info
    fields = '__all__'
    template_name = 'generic_form.html'
    permission_required = 'basic_management.change_company_info'

    def get_context_data(self, **kwargs):
        context = super(CompanyInfoUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Company info'
        return context


class CompanyInfoDelete(PermissionRequiredMixin, DeleteView):
    model = models.Company_Info
    fields = ['name']
    template_name = 'generic_confirm_delete.html'
    success_url = reverse_lazy('company-list')
    permission_required = 'basic_management.delete_company_info'

    def get_context_data(self, **kwargs):
        context = super(CompanyInfoDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Company info'
        return context


def company_search(request):
    company_Info = models.Company_Info
    name = request.GET.get('name')
    person_in_charge = request.GET.get('person_in_charge')
    phone = request.GET.get('phone')
    company_list = company_Info.objects.filter(
        person_in_charge__contains=person_in_charge).filter(name__contains=name).filter(phonenumber__contains=phone)
    return render(request, 'basic_management/company_info_search.html', {'company_list': company_list})
# =======employee=======================================


def employee_search(request):
    Employee_Info = models.Employee_Info
    name = request.GET.get('name')
    comp_id = request.GET.get('comp_id')
    user = request.GET.get('user')
    phone = request.GET.get('phone')
    employee_list = Employee_Info.objects.filter(name__contains=name).filter(
        comp_id__name__contains=comp_id).filter(phonenumber__contains=phone)
    if 'user' in request.GET and request.GET['user'] != '':
        employee_list = employee_list.filter(name__contains=name).filter(comp_id__name__contains=comp_id).filter(
            phonenumber__contains=phone).filter(user__username__contains=user)
    return render(request, 'basic_management/employee_info_search.html', {'employee_list': employee_list})


class EmployeeInfoCreate(PermissionRequiredMixin, CreateView):

    model = models.Employee_Info
    fields = '__all__'
    template_name = 'generic_form.html'
    permission_required = 'basic_management.add_employee_info'

    def get_context_data(self, **kwargs):
        context = super(EmployeeInfoCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Employee info create'
        return context


class EmployeeInfoUpdate(PermissionRequiredMixin, UpdateView):
    model = models.Employee_Info
    fields = '__all__'
    template_name = 'generic_form.html'
    permission_required = 'basic_management.change_employee_info'

    def get_context_data(self, **kwargs):
        context = super(EmployeeInfoUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Employee info update'
        return context


class EmployeeInfoDelete(PermissionRequiredMixin, DeleteView):
    model = models.Employee_Info
    fields = ['name']
    success_url = reverse_lazy('Employee-list')
    permission_required = 'basic_management.delete_employee_info'

    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeInfoDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Employee info'
        return context

# =======Client=======================================


def Client_search(request):
    client_Info = models.Client_Info
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    client_list = client_Info.objects.filter(
        name__contains=name).filter(phonenumber__contains=phone)
    return render(request, 'basic_management/client_info_list_search.html', {'client_list': client_list})


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


class ClientInfoCreate(PermissionRequiredMixin, CreateView):
    model = models.Client_Info
    template_name = 'generic_form.html'
    form_class = ClientInfoForm
    permission_required = 'basic_management.add_client_info'

    def get_context_data(self, **kwargs):
        context = super(ClientInfoCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Client info create'
        return context


class ClientInfoUpdate(ClientInfoCreate, UpdateView):

    permission_required = 'basic_management.change_client_info'

    def get_context_data(self, **kwargs):
        context = super(ClientInfoUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Client info update'
        return context


class ClientInfoDelete(PermissionRequiredMixin, DeleteView):
    model = models.Client_Info
    fields = ['name']
    success_url = reverse_lazy('client_info-list')
    permission_required = 'basic_management.delete_client_info'
    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(ClientInfoDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Client info'
        return context


# =======Product=======================================


def product_search(request):
    Product_Info = models.Product_Information
    name = request.GET.get('name')
    height = request.GET.get('height')
    weight = request.GET.get('weight')
    price = request.GET.get('price')
    categories_id = request.GET.get('categories_id')
    Product_list = Product_Info.objects.filter(categories_id__name__contains=categories_id).filter(
        price__contains=price).filter(weight__contains=weight).filter(height__contains=height).filter(name__contains=name)
    return render(request, 'basic_management/product_Informations_search.html', {'Product_list': Product_list})


class ProductInformationCreate(PermissionRequiredMixin, CreateView):
    model = models.Product_Information
    fields = '__all__'
    template_name = 'generic_form.html'
    permission_required = 'basic_management.add_product_information'

    def get_context_data(self, **kwargs):
        context = super(ProductInformationCreate,
                        self).get_context_data(**kwargs)
        context['table_name'] = 'Product information create'
        return context


class ProductInformationUpdate(PermissionRequiredMixin, UpdateView):
    model = models.Product_Information
    fields = '__all__'
    template_name = 'generic_form.html'
    permission_required = 'basic_management.change_product_information'

    def get_context_data(self, **kwargs):
        context = super(ProductInformationUpdate,
                        self).get_context_data(**kwargs)
        context['table_name'] = 'Product information update'
        return context


class ProductInformationDelete(PermissionRequiredMixin, DeleteView):
    model = models.Product_Information
    fields = ['name']
    success_url = reverse_lazy('product_information-list')
    permission_required = 'basic_management.delete_product_information'

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


class CategoriesCreate(PermissionRequiredMixin, CreateView):
    model = models.Categorie
    fields = '__all__'
    template_name = 'generic_form.html'
    permission_required = 'basic_management.add_categorie'

    def get_context_data(self, **kwargs):
        context = super(CategoriesCreate, self).get_context_data(**kwargs)
        context['table_name'] = 'Categorie create'
        return context


class CategoriesUpdate(PermissionRequiredMixin, UpdateView):
    model = models.Categorie
    fields = '__all__'
    template_name = 'generic_form.html'
    permission_required = 'basic_management.change_categorie'

    def get_context_data(self, **kwargs):
        context = super(CategoriesUpdate, self).get_context_data(**kwargs)
        context['table_name'] = 'Categorie update'
        return context


class CategorieDelete(PermissionRequiredMixin, DeleteView):
    model = models.Categorie
    fields = ['name']
    success_url = reverse_lazy('categories-list')
    template_name = 'generic_confirm_delete.html'
    permission_required = 'basic_management.delete_categorie'

    def get_context_data(self, **kwargs):
        context = super(CategorieDelete, self).get_context_data(**kwargs)
        context['table_name'] = 'Categorie'
        return context
# =======Manufacturer=======================================


def Manufacturer_search(request):
    Manufacturer_Info = models.Manufacturer_Information
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    person_in_charge = request.GET.get('person_in_charge')
    total = request.GET.get('total')
    Manufacturer_list = Manufacturer_Info.objects.filter(Total_capital__contains=name).filter(
        person_in_charge__contains=person_in_charge).filter(phonenumber__contains=phone).filter(name__contains=name)
    return render(request, 'basic_management/Manufacturer_Informations_search.html', {'Manufacturer_list': Manufacturer_list})


class ManufacturerInformationCreate(PermissionRequiredMixin, CreateView):
    model = models.Manufacturer_Information
    fields = '__all__'
    template_name = 'generic_form.html'
    permission_required = 'basic_management.add_manufacturer_information'

    def get_context_data(self, **kwargs):
        context = super(ManufacturerInformationCreate,
                        self).get_context_data(**kwargs)
        context['table_name'] = 'Manufacturer information create'
        return context


class ManufacturerInformationUpdate(PermissionRequiredMixin, UpdateView):
    model = models.Manufacturer_Information
    fields = '__all__'
    template_name = 'generic_form.html'
    permission_required = 'basic_management.change_manufacturer_information'

    def get_context_data(self, **kwargs):
        context = super(ManufacturerInformationUpdate,
                        self).get_context_data(**kwargs)
        context['table_name'] = 'Manufacturer information update'
        return context


class ManufacturerInformationDelete(PermissionRequiredMixin, DeleteView):
    model = models.Manufacturer_Information
    fields = ['name']
    success_url = reverse_lazy('manufacturer_information-list')
    permission_required = 'basic_management.delete_manufacturer_information'
    template_name = 'generic_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(ManufacturerInformationDelete,
                        self).get_context_data(**kwargs)
        context['table_name'] = 'Manufacturer information info'
        return context


def product_price_request(request):
    price = models.Product_Information.objects.get(
        pk=request.GET['product_id']).price
    return JsonResponse({'price': price})
