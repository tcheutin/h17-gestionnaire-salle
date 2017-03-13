# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 15:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auditorium', '0002_auto_20170310_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('i', 'In Progress'), ('o', 'Open for Purchase'), ('c', 'Closed')], default='i', max_length=1)),
                ('name', models.CharField(default='', help_text='Event Name', max_length=120)),
                ('image', models.ImageField(blank=True, default='', help_text='Event Image', upload_to='uploads/images/')),
                ('artist', models.CharField(default='', help_text='Artist Name', max_length=100)),
                ('isPublished', models.BooleanField(default=False)),
                ('isOnSale', models.BooleanField(default=False)),
                ('startDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('endDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('description', models.TextField(max_length=10000)),
                ('nbTickets', models.IntegerField(default=0)),
                ('ticketPrice', models.IntegerField(default=0)),
                ('auditorium', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auditorium.Auditorium')),
            ],
            options={
                'ordering': ['startDate', '-name'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique Ticket ID', primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('isReserved', models.BooleanField(default=False)),
                ('isSold', models.BooleanField(default=False)),
                ('isUsed', models.BooleanField(default=False)),
                ('event', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Event')),
            ],
        ),
    ]
