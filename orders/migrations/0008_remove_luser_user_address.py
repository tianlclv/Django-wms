# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-20 11:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20170804_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='luser',
            name='user_address',
        ),
    ]