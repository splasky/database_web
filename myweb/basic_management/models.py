#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-23 16:37:43

from django.db import models


class Company_Info(models.Model):
    comp_id = models.UUIDField(primary_key=True)
    comp_name = models.CharField(max_length=100)
    comp_address = models.EmailField(max_length=200)
    comp_phonenumber = models.CharField(max_length=200)
    comp_EIN = models.CharField(max_length=50)
    comp_person_in_charge = models.CharField(max_length=20)
    comp_NUM_employee = models.IntegerField()
    comp_email = models.CharField(max_length=254)
    comp_introduction = models.TextField(blank=True, null=True)


class Employee_Info(models.Model):
    emp_id = models.UUIDField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_address = models.EmailField(max_length=200)
    emp_phonenumber = models.CharField(max_length=200)
    emp_gender = models.BooleanField()
    emp_birthday = models.DateField()
    comp_id = models.ForeignKey(Company_Info, models.DO_NOTHING)


class Client_Info(models.Model):
    client_id = models.UUIDField(primary_key=True)
    client_name = models.CharField(max_length=100)
    client_address = models.EmailField(max_length=200)
    client_phonenumber = models.CharField(max_length=200)
    client_gender = models.BooleanField()
    client_birthday = models.DateField()


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
