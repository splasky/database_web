#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-28 11:14:00
from django.db import models
from django.urls import reverse


class Company_Info(models.Model):

    name = models.CharField('公司名稱', max_length=100)
    address = models.CharField('地址', max_length=200)
    phonenumber = models.CharField('公司電話', max_length=200)
    EIN = models.CharField('統一編號', max_length=50)
    person_in_charge = models.CharField('負責人', max_length=20)
    NUM_employee = models.IntegerField('公司人數', )
    email = models.EmailField(max_length=254)
    introduction = models.TextField('公司簡介', blank=True, null=True)

    class Mate:
        db_table = 'Company_Info'

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('company-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Employee_Info(models.Model):

    M = 'male'
    F = 'female'

    name = models.CharField('員工姓名', max_length=100)
    address = models.CharField('地址', max_length=200)
    email = models.EmailField(max_length=200, null=True)
    phonenumber = models.CharField('電話', max_length=200)
    EMP_gender = ((M, 'male'), (F, 'female'))
    gender = models.CharField('性別', max_length=6, choices=EMP_gender)

    birthday = models.DateField('生日', )
    comp_id = models.ForeignKey(Company_Info, models.DO_NOTHING)

    class Mate:
        db_table = 'Employee_Info'


class Client_Info(models.Model):
    M = 'male'
    F = 'female'

    name = models.CharField('客戶名稱', max_length=100)
    address = models.CharField('地址', max_length=200)
    email = models.EmailField(max_length=200, null=True)
    phonenumber = models.CharField('電話', max_length=200)
    CLIENT_gender = ((M, 'male'), (F, 'female'))
    gender = models.CharField('性別', max_length=6, choices=CLIENT_gender)
    birthday = models.DateField('生日', )

    class Mate:
        db_table = 'Client_Info'


class Categorie(models.Model):
    """Merchandise Categories"""
    Categorie_name = models.CharField('分類', max_length=100)

    class Mate:
        db_table = 'categories'


class Product_Information(models.Model):
    """Product's information"""
    Product_name = models.CharField('產品名稱', max_length=100)
    Hight = models.FloatField('高度', )
    Weight = models.FloatField('重量', )
    Categories_id = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    class Mate:
        db_table = 'product_information'


class Manufacturer_Information(Company_Info):
    """Manufacturer's information"""
    Total_capital = models.IntegerField('資本額', )

    class Mate:
        db_table = 'manufacturer information'
