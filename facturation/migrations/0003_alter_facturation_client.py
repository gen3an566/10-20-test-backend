# Generated by Django 4.0.4 on 2023-12-05 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facturation', '0002_alter_facturation_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturation',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
