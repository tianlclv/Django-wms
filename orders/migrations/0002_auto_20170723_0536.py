# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='luser',
            name='user_taobao',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='luser',
            name='user_address',
            field=models.ManyToManyField(null=True, to='orders.Address'),
        ),
        migrations.AlterField(
            model_name='luser',
            name='user_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='luser',
            name='user_eval',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='luser',
            name='user_phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='luser',
            name='user_qq',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='luser',
            name='user_weixin',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
