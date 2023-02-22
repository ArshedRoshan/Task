from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import Userserializer,cartmodel,userprofileSeriaizer
from.models import User
from django.core.mail import EmailMessage
import uuid
from product.serailizers import *

# Create your views here.
@api_view(['GET','POST'])
def add_user(request):
    user = request.data
    serializer = Userserializer(data=user,partial = True)
    if serializer.is_valid():
        serializer.save()
        # send_email(email)
        # cart_data = {'user': 1}
        # cart_serializer = cartmodel(data=cart_data)
        # if cart_serializer.is_valid():
        #     cart_serializer.save()
        user_profile = {'user':1}
        proserializer = userprofileSeriaizer(data=user_profile)
        if proserializer.is_valid():
            proserializer.save()
            return Response(200)
    return Response(serializer.errors)

@api_view(['GET','POST'])
def login(request):
    email = request.data['email']
    user = User.objects.filter(email = email)
    if user:
        return Response('You are logged in')
@api_view(['GET','POST'])
def get_users(request):
    user = User.objects.all()
    serializer = Userserializer(user,many = True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def send_email(email):
    subject = "Email verification"
    myuuid = uuid.uuid4()
    message = myuuid
    email_from = "arshaachu215@gmail.com"
    recipeint = [email]
    email = EmailMessage(subject=subject,body=message,to=recipeint)
    email.send() 
    



    


