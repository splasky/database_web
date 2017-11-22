from django.contrib import admin
from basic_management.models import *
# Register your models here.
class Company_InfoAdmin(admin.ModelAdmin):
	list_display=('comp_id',)

admin.site.register(Company_Info,Company_InfoAdmin)
admin.site.register(Employee_Info)
admin.site.register(Client_Info)
