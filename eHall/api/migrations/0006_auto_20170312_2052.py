# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170309_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terminal',
            name='netmask',
        ),
        migrations.RemoveField(
            model_name='terminal',
            name='token',
        ),
    ]
