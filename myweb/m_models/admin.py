# -*- coding:utf-8 -*-

from django.contrib import admin
from m_models.models import *


class AuthGroupAdmin(admin.ModelAdmin):
    list_display=('name')


class AuthGroupPermissionsAdmin(admin.ModelAdmin):
    list_display=('group', 'permission')


admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions, AuthGroupPermissionsAdmin)
