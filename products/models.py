import uuid,os

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.conf import settings
from django.dispatch import receiver

def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join("uploads/products/", filename)


class Product(models.Model):
    """Product model"""

    title = models.CharField(max_length=255, )
    the_cost = models.IntegerField(default=0)
    image = models.ImageField(null=True, upload_to=recipe_image_file_path, blank=True)
    description = models.TextField()
    
        
    def __str__(self):
        return self.title
