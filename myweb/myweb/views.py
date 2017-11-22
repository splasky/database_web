#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-11-21 22:27:20

from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html', locals())
