# Generated by Django 4.0.4 on 2023-12-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='facturation_adress',
            field=models.TextField(default=''),
        ),
    ]
