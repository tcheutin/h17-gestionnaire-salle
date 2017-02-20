from django.db import models

# Create your models here.

class Auditorium(models.Model):
    #Model representing an auditorium (e.g. Salle Alphonse, Salle Renommé).
    AUDITORIUM_STATUS = (
        ('c', 'Closed'),
        ('i', 'Empty'),
        ('o', 'Open'),
        ('f', 'Full'),
    )

    status = models.CharField(max_length=1, choices=AUDITORIUM_STATUS, blank=True, default='i', help_text='Auditorium status')
    name = models.CharField(max_length=50, help_text="Enter an auditorim name.")
    address = models.CharField(max_length=50, default='', help_text="Enter an address.")
    city = models.CharField(max_length=50, default='', help_text="Enter a city.")
    province = models.CharField(max_length=50, default='', help_text="Enter a province.")
    capacity = models.IntegerField(default=0)

    class Meta:
        ordering = ["status"]

        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name
