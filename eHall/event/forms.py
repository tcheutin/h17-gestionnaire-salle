from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from .models import Event

class AddForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

    class Meta:
        model = Event
        fields = ['name', 'artist', 'image', 'startDate', 'endDate', 'description', 'nbTickets', 'ticketPrice', 'auditorium']
        
class EditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

    class Meta:
        model = Event
        fields = ['name', 'artist', 'image', 'startDate', 'endDate', 'description', 'auditorium']

class PublishForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PublishForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

    class Meta:
        model = Event
        fields = ['retailer']
