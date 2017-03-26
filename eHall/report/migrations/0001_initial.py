# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 11:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0003_auto_20170324_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('httpResponse', models.CharField(default='', max_length=30)),
                ('time', models.DateTimeField(blank=True)),
                ('ticketHash', models.CharField(default=None, max_length=30)),
                ('terminal', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Terminal')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
