from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Terminal(models.Model):

    CONNECTION_STATUS = (('Connected', 'Connected'),
                         ('Ready', 'Ready'))

    id = models.AutoField(primary_key=True)

    event = models.ForeignKey(  'event.Event',
                                null=True,
                                on_delete=models.SET_NULL,
                                default='')

    status  = models.CharField( max_length=30,
                                choices=CONNECTION_STATUS,
                                default='Connected',
                                null=False,
                                blank=False)

    address = models.CharField( max_length=30,
                                null=False,
                                blank=False,
                                unique=True)
    class Meta:
        ordering = ["id"]

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.address
