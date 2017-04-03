from django.db import models
from datetime import datetime

# Create your models here.
class Report(models.Model):
    id = models.AutoField(primary_key=True)

    terminal = models.ForeignKey(  'api.Terminal',
                                    null=True,
                                    on_delete=models.SET_NULL,
                                    default='')

    httpResponse = models.CharField(max_length=120, default='')
    time = models.DateTimeField(blank=True)
    ticketHash = models.CharField(max_length=120, default=None)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.httpResponse
