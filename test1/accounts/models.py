from django.db import models
from product.models import *

# Create your models here.
class User(models.Model):
    phone_number = models.IntegerField(unique=True)
    Email = models.EmailField()
    is_customer = models.BooleanField()
    is_admin = models.BooleanField()

class userProfileModel(models.Model):
    Gender = (
        ("1","Male"),
        ("2","Female"),
        ("3","Others")
    )
    owner = models.OneToOneField(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    Date_of_birth = models.CharField(max_length=30)
    gender = models.CharField(max_length=30,choices=Gender)

class userloginotp(models.Model):
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    otp = models.IntegerField()
    active = models.BooleanField()

class UserCartProductModel(models.Model):
    status = (
        ("1","pending"),
        ("2","completed")
    )
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    Status = models.CharField(max_length=10,choices=status)

class UserCartModel:
    owner = models.OneToOneField(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(UserCartProductModel)
    price = models.IntegerField
    
   
   

    
