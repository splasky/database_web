#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-22 19:45:00

from django.db import models


class Categories(models.Model):

    """Merchandise Categories"""
    Categories_id = models.UUIDField(primary_key=True)
    Categories_name = models.CharField(max_length=100)

    class Mate:
        db_table = 'categories'


class Product_Information(models.Model):

    """Product's information"""
    Product_id = models.UUIDField(primary_key=True)
    Product_name = models.CharField(max_length=100)
    Hight = models.FloatField()
    Weight = models.FloatField()
    Categories_id = models.ForeignKey('Categories', on_delete=models.CASCADE)

    class Mate:
        db_table = 'product_information'


class Manufacturer_Information(models.Model):

    """Manufacturer's information"""
    Manufacturer_id = models.UUIDField(primary_key=True)
    Uniform_numbers = models.CharField(max_length=100)
    ManuFacturer_name = models.CharField(max_length=100)
    Total_capital = models.IntegerField()
    Name_of_representative = models.CharField(max=100)
    Company_location = models.CharField(max=200)

    class Mate:
        db_table = 'manufacturer information'
