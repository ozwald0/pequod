# Generated by Django 5.1 on 2024-08-26 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vanguard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_images',
        ),
    ]
