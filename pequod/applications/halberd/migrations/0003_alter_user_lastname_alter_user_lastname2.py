# Generated by Django 5.1 on 2024-08-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halberd', '0002_alter_user_validation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname2',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
