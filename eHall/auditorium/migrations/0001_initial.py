# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 14:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditorium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('c', 'Closed'), ('i', 'Empty'), ('o', 'Open'), ('f', 'Full')], default='i', help_text='Auditorium status', max_length=1)),
                ('name', models.CharField(help_text='Enter an auditorium name.', max_length=50)),
                ('address', models.CharField(default='', help_text='Enter an address.', max_length=50)),
                ('city', models.CharField(default='', help_text='Enter a city.', max_length=50)),
                ('province', models.CharField(default='', help_text='Enter a province.', max_length=50)),
                ('capacity', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['status'],
            },
        ),
    ]
