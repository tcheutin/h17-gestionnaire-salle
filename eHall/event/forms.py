from django import forms
from eHall.event.models import Event
from eHall.auditorium.models import Auditorium

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'artist', 'image', 'startDate', 'endDate', 'description', 'auditorium',)
