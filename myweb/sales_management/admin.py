from django.contrib import admin
from sales_management.models import *

class Basic_Info_Admin(admin.ModelAdmin):
    list_display = ('id', 'date','client_id')
    search_fields = ('id', 'date','client_id')

    class Mate:
        abstract = True

class Sales_InfoAdmin(Basic_Info_Admin):
    pass

class Returns_InfoAdmin(Basic_Info_Admin):
    pass

class Order_InfoAdmin(Basic_Info_Admin):
    pass

class Basic_Details_Admin(admin.ModelAdmin):
    list_display=('')
    search_fields = ('')

    class Mate:
        abstract = True

class Order_DetailsAdmin(Basic_Details_Admin):
    pass

class Sales_DetailsAdmin(Basic_Details_Admin):
    pass

class Returns_DetailsAdmin(Basic_Details_Admin):
    pass

admin.site.register(Sales_Info, Sales_InfoAdmin)
admin.site.register(Returns_Info, Returns_InfoAdmin)
admin.site.register(Order_Info, Order_InfoAdmin)
admin.site.register(Order_Details, Order_DetailsAdmin)
admin.site.register(Sales_Details, Sales_DetailsAdmin)
admin.site.register(Returns_Details, Returns_DetailsAdmin)