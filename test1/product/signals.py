from django.db.models.signals import pre_save
from django.dispatch import receiver
from product.models import productMainModel
import uuid

@receiver(pre_save,sender = productMainModel)
def generate_id(sender,instance,**kwargs):
    if not instance.Unique_id:
        instance.Unique_id = uuid.uuid4().hex