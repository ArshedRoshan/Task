from django.db import models

# Create your models here.

class productMainModel(models.Model):
    Title = models.CharField(max_length=30)
    Description = models.TextField()
    Unique_id = models.CharField(max_length=1000,unique=True)
    price = models.IntegerField()

class productImageModel(models.Model):
    product = models.ForeignKey(productMainModel,on_delete=models.CASCADE,related_name='proo')
    image  = models.ImageField()