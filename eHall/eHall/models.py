from django.db import models
import uuid # Required for unique ticket instances

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique Ticket ID')
    owner = models.CharField(max_length=100, default='', help_text="People")
    event = models.ForeignKey('event.Event', null=True, on_delete=models.SET_NULL, default='')
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    isReserved = models.BooleanField(default=False)
    isSold = models.BooleanField(default=False)
    scannedBy = models.ForeignKey('api.Terminal', null=True, on_delete=models.PROTECT)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.id