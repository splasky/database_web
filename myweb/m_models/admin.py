# -*- coding:utf-8 -*-

from django.contrib import admin
from m_models.models import *


class AuthGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AuthGroupPermissionsAdmin(admin.ModelAdmin):
    list_display = ('group', 'permission')


class AuthPermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'codename')


class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('password', 'last_login', 'is_superuser', 'username',
                    'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('first_name',)


class AuthUserGroupsAdmin(admin.ModelAdmin):
    list_display = ('user', 'group')


class AuthUserUserPermissionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'permission')


class DjangoAdminLogAdmin(admin.ModelAdmin):
    list_display = ('action_time', 'object_id', 'object_repr',
                    'action_flag', 'change_message', 'content_type', 'user')


class DjangoContentTypeAdmin(admin.ModelAdmin):
    list_display = ('app_label', 'model')


class DjangoMigrationsAdmin(admin.ModelAdmin):
    list_display = ('app', 'name', 'applied')


class DjangoSessionAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'session_data', 'expire_date')


admin.site.register(AuthGroup, AuthGroupAdmin)
admin.site.register(AuthGroupPermissions, AuthGroupPermissionsAdmin)
admin.site.register(AuthPermission, AuthPermissionAdmin)
admin.site.register(AuthUser, AuthUserAdmin)
admin.site.register(AuthUserGroups, AuthUserGroupsAdmin)
admin.site.register(AuthUserUserPermissions, AuthUserUserPermissionsAdmin)
admin.site.register(DjangoAdminLog, DjangoAdminLogAdmin)
admin.site.register(DjangoContentType, DjangoContentTypeAdmin)
admin.site.register(DjangoMigrations, DjangoMigrationsAdmin)
admin.site.register(DjangoSession, DjangoSessionAdmin)
