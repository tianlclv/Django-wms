# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20170729_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luser',
            name='user_address',
            field=models.ManyToManyField(blank=True, to='orders.Address'),
        ),
    ]
