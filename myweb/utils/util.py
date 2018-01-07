#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2018-01-03 20:51:53

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def generic_list(request, app, model, table_name=''):
    objects = model.objects.all()
    table_name = table_name
    paginate_by = 10
    return render(request,
                  '{}/{}s_list.html'.format(app,
                      model.__name__.lower()),
                  locals())


@login_required
def generic_detail(request, pk, app, model, table_name=''):
    object = model.objects.get(id=pk)
    table_name = table_name

    return render(request,
                  '{}/{}s_detail.html'.format(app,
                      model.__name__.lower()),
                  locals())
