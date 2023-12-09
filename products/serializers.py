from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from .models import Product


class ProductsSerializer(serializers.ModelSerializer):
    """Serializer for products"""

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("id",)



class ProductImageSerializer(serializers.ModelSerializer):
    """Serializer for image uploading"""

    class Meta:
        model = Product
        fields = ("id", "image")
        read_only_fields = ("id",)