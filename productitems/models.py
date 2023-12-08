from django.db import models

from django.db import models
from django.conf import settings

class ProductItem(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)        


    def __str__(self):
        return f"{self.quantity},{self.product}"