from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from custom_permissions.IsStaffUser import SomeModelPermission, IsAdminUser
from custom_permissions.CanJustReadPermissions import CanJustPostOrIsAdminPermission,CanJustReadOrIsAdminPermission
from .models import Product
from . import serializers

class ProductsViewSet(viewsets.ModelViewSet):
    """Manage Products in the db"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (CanJustReadOrIsAdminPermission,)
    queryset = Product.objects.all().order_by('-id')
    serializer_class = serializers.ProductsSerializer
    pagination_class = None

    def _params_to_int(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(",")]
       
    
    def get_queryset(self):
        """Retrieve the nfts from the query params sended"""

        return Product.objects.all().order_by('-id')
    
    def get_serializer_class(self):
        if self.action == "upload_image":
            return serializers.ProductImageSerializer
        
        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()



    @action(methods=["POST"], detail=True, url_path="upload-image")
    def upload_image(self, request, id=None):
        """Upload image"""
        recipe = self.get_object()
        serializer = self.get_serializer(
            recipe,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )