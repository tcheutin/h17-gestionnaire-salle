from django.db import models

# Create your models here.
class Terminal(models.Model):

    CONNECTION_STATUS = (('Connected', 'Connected'),
                         ('Ready', 'Ready'))

    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=90, null=False, blank=False)
    status  = models.CharField( max_length=30,
                                choices=CONNECTION_STATUS,
                                default='Connected',
                                null=False,
                                blank=False)
    ipAddress = models.CharField(max_length=30, null=False, blank=False)
