# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django import template
from django.http import HttpResponseRedirect


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())

def index(request):
    return render(request, 'index.html', locals())
