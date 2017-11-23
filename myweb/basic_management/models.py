#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-23 16:37:43

from django.db import models


class Company_Info(models.Model):
    comp_name = models.CharField(max_length=100)
    comp_address = models.CharField(max_length=200)
    comp_phonenumber = models.CharField(max_length=200)
    comp_EIN = models.CharField(max_length=50)
    comp_person_in_charge = models.CharField(max_length=20)
    comp_NUM_employee = models.IntegerField()
    comp_email = models.EmailField(max_length=254)
    comp_introduction = models.TextField(blank=True, null=True)

    class Mate:
        db_table = 'Company_Info'


class Employee_Info(models.Model):
    M = 'male'
    F = 'female'

    emp_name = models.CharField(max_length=100)
    emp_address = models.CharField(max_length=200)
    emp_email = models.EmailField(max_length=200, null=True)
    emp_phonenumber = models.CharField(max_length=200)
    EMP_gender = ((M, 'male'), (F, 'female'))
    emp_gender = models.CharField(max_length=2, choices=EMP_gender)

    emp_birthday = models.DateField()
    comp_id = models.ForeignKey(Company_Info, models.DO_NOTHING)

    class Mate:
        db_table = 'Employee_Info'


class Client_Info(models.Model):
    M = 'male'
    F = 'female'

    client_name = models.CharField(max_length=100)
    client_address = models.CharField(max_length=200)
    client_email = models.EmailField(max_length=200, null=True)
    client_phonenumber = models.CharField(max_length=200)
    CLIENT_gender = ((M, 'male'), (F, 'female'))
    client_gender = models.CharField(max_length=2, choices=CLIENT_gender)
    client_birthday = models.DateField()

    class Mate:
        db_table = 'Client_Info'


class Categories(models.Model):

    """Merchandise Categories"""
    Categories_name = models.CharField(max_length=100)

    class Mate:
        db_table = 'categories'


class Product_Information(models.Model):

    """Product's information"""
    Product_name = models.CharField(max_length=100)
    Hight = models.FloatField()
    Weight = models.FloatField()
    Categories_id = models.ForeignKey('Categories', on_delete=models.CASCADE)

    class Mate:
        db_table = 'product_information'


class Manufacturer_Information(models.Model):

    """Manufacturer's information"""
    Uniform_numbers = models.CharField(max_length=100)
    ManuFacturer_name = models.CharField(max_length=100)
    Total_capital = models.IntegerField()
    Name_of_representative = models.CharField(max_length=100)
    Company_location = models.CharField(max_length=200)

    class Mate:
        db_table = 'manufacturer information'
