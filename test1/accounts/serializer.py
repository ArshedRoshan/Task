from rest_framework import serializers
from . models import User,UserCartProductModel,userProfileModel

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone_number","Email","is_customer","is_admin"]
class userprofileSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = userProfileModel
        fields = "__all__"

class cartmodel(serializers.ModelSerializer):
    class Meta:
        model = UserCartProductModel
        fields = "__all__"
    