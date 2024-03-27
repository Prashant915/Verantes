from django.db import models
from django.contrib.auth.models import User

class Customer_Detail(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Phone_Number=models.CharField(max_length=12,null=False,blank=False)
    City=models.CharField(max_length=50)
    Looking_For=models.CharField(max_length=50)
    Budget=models.CharField(max_length=50)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=20)
    whatsapp_status=models.CharField(max_length=10)
    email=models.CharField(max_length=50,default=None)
    pincode=models.CharField(max_length=6,default=None)