# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Connected', 'Connected'), ('Ready', 'Ready')], default='Connected', max_length=30)),
                ('address', models.CharField(max_length=30, unique=True)),
                ('event', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Event')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
