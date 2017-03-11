from django import forms
from crispy_forms.helper import FormHelper
from .models import Event
from auditorium.models import Auditorium

class AddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

    class Meta:
        model = Event
        fields = ('name', 'artist', 'image', 'startDate', 'endDate', 'description', 'auditorium',)
        
class EditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

    class Meta:
        model = Event
        fields = ('name', 'artist', 'image', 'startDate', 'endDate', 'description', 'auditorium',)
        
class DeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

    class Meta:
        model = Event
        fields = ('name', 'artist', 'image', 'startDate', 'endDate', 'description', 'auditorium',)
