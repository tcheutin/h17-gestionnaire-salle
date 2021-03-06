# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 14:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auditorium', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('i', 'In Progress'), ('o', 'Open for Purchase'), ('c', 'Closed')], default='i', max_length=1)),
                ('name', models.CharField(default='', help_text='Event Name', max_length=120)),
                ('image', models.URLField(default='')),
                ('artist', models.CharField(default='', help_text='Artist Name', max_length=100)),
                ('isPublished', models.BooleanField(default=False)),
                ('isOnSale', models.BooleanField(default=False)),
                ('startDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('endDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('description', models.TextField(max_length=10000)),
                ('nbTickets', models.IntegerField(default=0)),
                ('ticketPrice', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('isClose', models.BooleanField(default=True)),
                ('auditorium', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auditorium.Auditorium')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['startDate', '-name'],
            },
        ),
        migrations.CreateModel(
            name='TicketRetailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('url', models.URLField(default='')),
                ('key', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='retailer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.TicketRetailer'),
        ),
    ]
