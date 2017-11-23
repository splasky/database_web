# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 05:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client_Info',
            fields=[
                ('client_id', models.UUIDField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=100)),
                ('client_address', models.EmailField(max_length=200)),
                ('client_phonenumber', models.CharField(max_length=200)),
                ('client_gender', models.BooleanField()),
                ('client_birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Company_Info',
            fields=[
                ('comp_id', models.UUIDField(primary_key=True, serialize=False)),
                ('comp_name', models.CharField(max_length=100)),
                ('comp_address', models.EmailField(max_length=200)),
                ('comp_phonenumber', models.CharField(max_length=200)),
                ('comp_EIN', models.CharField(max_length=50)),
                ('comp_person_in_charge', models.CharField(max_length=20)),
                ('comp_NUM_employee', models.IntegerField()),
                ('comp_email', models.CharField(max_length=254)),
                ('comp_introduction', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Info',
            fields=[
                ('emp_id', models.UUIDField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_address', models.EmailField(max_length=200)),
                ('emp_phonenumber', models.CharField(max_length=200)),
                ('emp_gender', models.BooleanField()),
                ('emp_birthday', models.DateField()),
                ('comp_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basic_management.Company_Info')),
            ],
        ),
    ]
