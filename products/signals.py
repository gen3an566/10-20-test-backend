from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product

@receiver(post_save,sender=Product)
def refresh_instance(sender,instance,**kwargs):
    instance.refresh_from_db()