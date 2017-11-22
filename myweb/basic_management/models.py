from django.db import models

# Create your models here.


class Company_Info(models.Model):
    comp_id = models.UUIDField(primary_key=True)
    comp_name = models.CharField(max_length=100)
    comp_address = models.EmialField(max_length=200)
    comp_phonenumber = models.CharField(max_length=200)
    comp_EIN = models.CharField(max_length=50)
    comp_person_in_charge = models.CharField(max_length=20)
    comp_NUM_employee = models.IntegerField()
    comp_email = models.CharField(max_length=254)
    comp_introduction=models.TextField(blank=True,null=True)


class Employee_Info(models.Model):
	emp_id = models.UUIDField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_address = models.EmailField(max_length=200)
    emp_phonenumber = models.CharField(max_length=200)
    emp_gender = models.BooleanField()
    emp_birthday = models.DateField()
    comp_id=models.Foreignkey(Company_Info,models.DO_NOTHING)

class Client_Info(models.Model):
	client_id = models.UUIDField(primary_key=True)
    client_name = models.CharField(max_length=100)
    client_address = models.EmailField(max_length=200)
    client_phonenumber = models.CharField(max_length=200)
    client_gender = models.BooleanField()
    client_birthday = models.DateField()