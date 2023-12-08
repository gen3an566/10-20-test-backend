from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from custom_permissions.IsStaffUser import SomeModelPermission, IsAdminUser
from custom_permissions.CanJustReadPermissions import CanJustPostOrIsAdminPermission
from .models import Facturation
from . import serializers


class FacturationsViewSet(viewsets.ModelViewSet):
    """Manage Facturations in the db"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (CanJustPostOrIsAdminPermission,)
    queryset = Facturation.objects.all().order_by("-id")
    serializer_class = serializers.FacturationSerializer
    pagination_class = None

    def _params_to_int(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(",")]
    
    def get_queryset(self):
        """Retrieve the nfts from the query params sended"""

        # query_search_by_title = self.request.query_params.get("user")
        # queryset = self.queryset
        # print("Search------------------------------------------------------------", query_search_by_title)

        # if query_search_by_title:
        #     return queryset.filter(posted_by=query_search_by_title)
        return Facturation.objects.all().order_by("-id")


    # def get_queryset(self):
    #     """Retrieve the nfts from the query params sended"""

    #     query_search_by_title = self.request.query_params.get("search")
    #     queryset = self.queryset
    #     print("Search------------------------------------------------------------", query_search_by_title)

    #     if query_search_by_title:
    #         query_search_by_ids = self._params_to_int(query_search_by_title)

    #         for idMe in query_search_by_ids:
    #             queryset = queryset.filter(members__id__in=[idMe])
    #         print("Va en pais------------------------------------------------------------", query_search_by_ids)

    #         return queryset.distinct()

    #     return queryset
    
    
    def get_serializer_class(self):
        """Return appropriate serializer class"""

        if self.action == "list":
                  
            return serializers.FacturationDetailledSerializer

        # if self.action == "followers_updates":
        #     return serializers.IdentityChatterFollowersSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(client=self.request.user)
