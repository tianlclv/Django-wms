# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-04 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20170804_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_class',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_province',
            field=models.CharField(max_length=20),
        ),
    ]