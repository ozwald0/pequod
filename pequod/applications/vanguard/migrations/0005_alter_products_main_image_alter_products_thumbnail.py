# Generated by Django 5.1 on 2024-08-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vanguard', '0004_alter_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='vanguard'),
        ),
        migrations.AlterField(
            model_name='products',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='vanguard'),
        ),
    ]
