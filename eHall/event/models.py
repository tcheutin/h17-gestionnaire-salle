from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

class Event(models.Model):
    STATUSES = (
        ('i', 'In Progress'),
        ('o', 'Open for Purchase'),
        ('c', 'Closed'),
    )

    status = models.CharField(max_length=1, choices=STATUSES, blank=True, default='i')
    name = models.CharField(max_length=120, default='', help_text='Event Name')
    image = models.URLField(max_length=200, default='', null=False)
    artist = models.CharField(max_length=100, default='', help_text='Artist Name')
    isPublished = models.BooleanField(default=False)
    isOnSale = models.BooleanField(default=False)
    startDate = models.DateTimeField(blank=True, default=timezone.now)
    endDate = models.DateTimeField(blank=True, default=timezone.now)
    description = models.TextField(max_length=10000)
    nbTickets = models.IntegerField(default=0)
    ticketPrice = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    auditorium = models.ForeignKey('auditorium.Auditorium', null=True, on_delete=models.SET_NULL)
    retailer = models.ForeignKey('TicketRetailer', null=True, on_delete=models.SET_NULL)
    creator = models.ForeignKey(User, null=True)
    isClose = models.BooleanField(default=True)

    # Metadata
    class Meta:
        ordering = ["startDate", "-name"]

    # Methods
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('event-detail', args=[str(self.id)])

    def getNbTicketsScanned(self, terminal):
        return Ticket.objects.filter(event = self, scannedBy_id = terminal).count()

        
class TicketRetailer(models.Model):
    name = models.CharField(max_length=100, default='', null=False)
    url = models.URLField(max_length=200, default='', null=False)
    key = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
