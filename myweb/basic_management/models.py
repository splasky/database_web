#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-23 19:24:52
from django.db import models


class Company_Info(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    EIN = models.CharField(max_length=50)
    person_in_charge = models.CharField(max_length=20)
    NUM_employee = models.IntegerField()
    email = models.EmailField(max_length=254)
    introduction = models.TextField(blank=True, null=True)

    class Mate:
        db_table = 'Company_Info'


class Employee_Info(models.Model):

    M = 'male'
    F = 'female'

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)
    phonenumber = models.CharField(max_length=200)
    EMP_gender = ((M, 'male'), (F, 'female'))
    gender = models.CharField(max_length=6, choices=EMP_gender)

    birthday = models.DateField()
    comp_id = models.ForeignKey(Company_Info, models.DO_NOTHING)

    class Mate:
        db_table = 'Employee_Info'


class Client_Info(models.Model):
    M = 'male'
    F = 'female'

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)
    phonenumber = models.CharField(max_length=200)
    CLIENT_gender = ((M, 'male'), (F, 'female'))
    gender = models.CharField(max_length=6, choices=CLIENT_gender)
    birthday = models.DateField()

    class Mate:
        db_table = 'Client_Info'


class Categorie(models.Model):

    """Merchandise Categories"""
    Categorie_name = models.CharField(max_length=100)

    class Mate:
        db_table = 'categories'


class Product_Information(models.Model):

    """Product's information"""
    Product_name = models.CharField(max_length=100)
    Hight = models.FloatField()
    Weight = models.FloatField()
    Categories_id = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    class Mate:
        db_table = 'product_information'


class Manufacturer_Information(Company_Info):

    """Manufacturer's information"""
    Uniform_numbers = models.CharField(max_length=100)
    Total_capital = models.IntegerField()

    class Mate:
        db_table = 'manufacturer information'
