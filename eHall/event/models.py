from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Event(models.Model):
    # To review
    STATUSES = (
        ('i', 'In Progress'),
        ('o', 'Open for Purchase'),
        ('c', 'Closed'),
    )

    status = models.CharField(max_length=1, choices=STATUSES, blank=True, default='i')
    name = models.CharField(max_length=120, default='', help_text='Event Name')
    image = models.ImageField(default='', blank=True, upload_to='uploads/images/', help_text='Event Image')
    artist = models.CharField(max_length=100, default='', help_text='Artist Name')
    isPublished = models.BooleanField(default=False)
    isOnSale = models.BooleanField(default=False)
    startDate = models.DateTimeField(blank=True, default=timezone.now)
    endDate = models.DateTimeField(blank=True, default=timezone.now)
    description = models.TextField(max_length=10000)
    nbTickets = models.IntegerField(default=0)
    auditorium = models.ForeignKey('auditorium.Auditorium', null=True, on_delete=models.SET_NULL)

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


import uuid # Required for unique ticket instances

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ticket ID')
    owner = models.CharField(max_length=100, default='', help_text="People")
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL, default='')
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    isReserved = models.BooleanField(default=False)
    isSold = models.BooleanField(default=False)
    isUsed = models.BooleanField(default=False)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.id
