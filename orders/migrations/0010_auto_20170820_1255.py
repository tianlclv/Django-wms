# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-20 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_luser_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_full',
            field=models.TextField(blank=True, null=True),
        ),
    ]
