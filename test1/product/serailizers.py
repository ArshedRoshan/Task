from rest_framework import serializers
from . models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = productImageModel
        fields = ['product','image']


class ProductSerializer(serializers.ModelSerializer):
    proo = ImageSerializer(many = True) # nested serializer
    class Meta:
        model = productMainModel
        fields = ["Title","Description","Unique_id","price","proo"]
        