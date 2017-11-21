#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-21 09:52:30

from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext


def login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/')

    return render(request, 'login.html', locals())


def index(request):
    return render(request, 'index.html', locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
