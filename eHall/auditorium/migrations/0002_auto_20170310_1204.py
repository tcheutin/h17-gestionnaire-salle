# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditorium', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditorium',
            name='name',
            field=models.CharField(help_text='Enter an auditorium name.', max_length=50),
        ),
    ]
