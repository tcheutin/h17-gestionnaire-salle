# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='ticketHash',
            field=models.CharField(default=None, max_length=120),
        ),
    ]
