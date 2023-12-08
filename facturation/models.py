import uuid,os

from django.db import models
from django.conf import settings


class Facturation(models.Model):
    """Facturation model"""
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('S', 'Solded'),
    )
    created_at = models.DateField(auto_now=True)
    products_items = models.ManyToManyField("productitems.ProductItem", blank=True)
    tva = models.IntegerField(default=18)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default="P")
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
