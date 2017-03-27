# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '__first__'),
        ('event', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique Ticket ID', primary_key=True, serialize=False)),
                ('owner', models.CharField(default='', help_text='People', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('isReserved', models.BooleanField(default=False)),
                ('isSold', models.BooleanField(default=False)),
                ('event', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Event')),
                ('scannedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.Terminal')),
            ],
        ),
    ]
