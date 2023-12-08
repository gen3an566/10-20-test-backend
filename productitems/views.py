from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from custom_permissions.IsStaffUser import SomeModelPermission, IsAdminUser
from .models import ProductItem
from . import serializers

class ProductsItemsViewSet(viewsets.ModelViewSet):
    """Manage ProductsItems in the db"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = ProductItem.objects.all().order_by('-id')
    serializer_class = serializers.ProductItemsSerializer
    pagination_class = None
    
    def get_queryset(self):
        """Retrieve the nfts from the query params sended"""

        return ProductItem.objects.all().order_by('-id')

    def perform_create(self, serializer):
        """Create a new object"""
        instance = serializer.save()

