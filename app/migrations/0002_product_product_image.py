# Generated by Django 5.0.6 on 2024-06-21 06:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='productimg'),
            preserve_default=False,
        ),
    ]
