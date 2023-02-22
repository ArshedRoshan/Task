from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serailizers import ProductSerializer,ImageSerializer
from.models import *
from accounts.models import UserCartModel,UserCartProductModel
from accounts.serializer import cartmodel

# Create your views here.
@api_view(['GET','POST'])
def add_product(request):
    pro = request.data
    serializer = ProductSerializer(data = pro,partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(200)
    return Response(serializer.errors)

@api_view(['GET','POST'])
def add_image(request,id):
    product = productMainModel.objects.get(id=id)
    img  = request.data
    serializer = ImageSerializer(data = img,product = product,partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(200)
    return Response(serializer.errors)

@api_view(['GET','POST'])
def get_product(request):
    pro = productMainModel.objects.all()
    # ImageSerializer is nested to ProductSerializer
    serializer = ProductSerializer(pro,many = True) 
    return Response(serializer.data)

@api_view(['GET','POST'])
def add_to_cart(request,product_id):
    print('request',request.data)
    try:
        product = productMainModel.objects.get(id = product_id)
        print('prooo',product)
    except productMainModel.DoesNotExist:
        return Response({'error':'Product not found'})
    try:
        cart_item = UserCartProductModel.objects.get(owner = ['user'],product = product)
        return Response(cartmodel(cart_item.data))
    except:
        pass
    cart_item = UserCartProductModel(owner =['user'],product = product)
    serializer = cartmodel(cart_item)
    if serializer.is_valid():
        return Response(200)
    
    