# Generated by Django 4.0.4 on 2023-12-07 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturation', '0004_remove_facturation_products_cartitem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
    ]
