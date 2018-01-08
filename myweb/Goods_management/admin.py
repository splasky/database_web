from django.contrib import admin
from Goods_management.models import *

class MasterAdmin(admin.ModelAdmin):
    list_display = ('Manufacturer_Info', 'date','staff',)


    class Mate:
        abstract = True


admin.site.register(Master, MasterAdmin)
