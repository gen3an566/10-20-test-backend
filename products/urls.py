
app_name = "products"


from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("", views.ProductsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
