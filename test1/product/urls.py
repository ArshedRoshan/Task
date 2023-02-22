from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
  path('add_product',add_product,name='add_product'),
  path('get_product',get_product,name='get_product'),
  path('add_to_cart/<int:product_id>',add_to_cart,name='add_to_cart')
]