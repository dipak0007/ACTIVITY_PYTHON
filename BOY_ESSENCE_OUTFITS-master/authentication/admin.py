from django.contrib import admin
from .models import MyCustomerModel, MyAddressModel

class MyCustomerModelAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'firstname', 'lastname', 'email', 'mobile', 'is_activate', 'is_added_address', 'otp')
    search_fields = ('firstname', 'lastname', 'email', 'mobile')  
    list_filter = ('is_activate', 'is_added_address')  
class MyAddressModelAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'curent_address', 'city', 'pincode', 'state')  
    search_fields = ('customer_id__firstname', 'customer_id__lastname', 'curent_address', 'city', 'pincode', 'state') 
    list_filter = ('city', 'state')  
admin.site.register(MyCustomerModel, MyCustomerModelAdmin)
admin.site.register(MyAddressModel, MyAddressModelAdmin)
