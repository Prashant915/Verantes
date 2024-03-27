from django.contrib import admin
from .models import *
# Register your models here.
class Customer(admin.ModelAdmin):
    list_display=("Name","Email","Phone_Number","City","Looking_For","Budget")

# class Signup(admin.ModelAdmin):
#     list_display=("Name","Phone_Number","Email","Pincode")

# admin.site.register(User,Signup)
class client(admin.ModelAdmin):
    list_display=("user","mobile","whatsapp_status","email","pincode")

admin.site.register(Profile,client)
admin.site.register(Customer_Detail,Customer)