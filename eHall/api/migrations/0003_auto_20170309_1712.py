# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170309_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='terminal',
            name='netmask',
            field=models.CharField(default='0.0.0.0', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='terminal',
            name='ipAddress',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
