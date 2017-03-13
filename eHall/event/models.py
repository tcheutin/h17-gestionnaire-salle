from django.db import models
from datetime import datetime

# Create your models here.
class Event(models.Model):
    STATUSES = (
        ('i', 'In progress'),
        ('o', 'Open for purchase'),
        ('c', 'Closed'),
    )

    status = models.CharField(max_length=1, choices=STATUSES, blank=True, default='i', help_text='Event current status')
    title = models.CharField(max_length=100, default='', help_text="Event's name")
    sticker = models.ImageField(default='') # TODO:
    image = models.ImageField(default='') # TODO:
    artist = models.CharField(max_length=100, default='', help_text="Artist's name")
    isPublished = models.BooleanField(default=False)
    isOnSale = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    duration = models.DurationField() # TODO: verifiy with other team
    description = models.TextField(max_length=500, help_text='Enter a brief description of the event')
    auditorium = models.ForeignKey('auditorium.Auditorium', on_delete=models.CASCADE)


    # Metadata
    class Meta:
        ordering = ["date", "-title"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    def __str__(self):
        return self.ticket

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('event-detail', args=[str(self.id)])


import uuid # Required for unique ticket instances

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this ticket")
    owner = models.CharField(max_length=100, default='', help_text="People")
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL, default='')
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    isReserved = models.BooleanField(default=False)
    isSold = models.BooleanField(default=False)
