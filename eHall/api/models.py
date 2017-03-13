from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Terminal(models.Model):

    CONNECTION_STATUS = (('Connected', 'Connected'),
                         ('Ready', 'Ready'))

    id = models.AutoField(primary_key=True)

    status  = models.CharField( max_length=30,
                                choices=CONNECTION_STATUS,
                                default='Connected',
                                null=False,
                                blank=False)
                                
    address = models.CharField( max_length=30,
                                null=False,
                                blank=False,
                                unique=True)
