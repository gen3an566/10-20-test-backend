from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from .models import Facturation
from productitems.models import ProductItem
from products.models import Product

from core.models import User
class ProductDetailSerializer(serializers.ModelSerializer):
    """Serialisers for product objects"""

    class Meta:
        model = Product
        fields = ("id", "title", "the_cost")
        read_only_fields = ("id",)


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ['id', 'product', 'quantity']


class FacturationSerializer(serializers.ModelSerializer):
    """Serializer for Facturation"""
    # products = ProductDetailSerializer(many=True)
        
    class Meta:
        model = Facturation
        fields = "__all__"
        read_only_fields = ("id","client", "tva")
        
class UserReducedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']
        

class FacturationDetailledSerializer(FacturationSerializer):
    """Serialisers for Facturation detail objects"""
    
    products_items = CartItemSerializer(many=True)
    client = UserReducedSerializer()