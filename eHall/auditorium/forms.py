from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from .models import Auditorium

class AddForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

    class Meta:
        model = Auditorium
        fields = ['name', 'image', 'address', 'postalCode', 'city', 'province', 'capacity']
        
class EditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

    class Meta:
        model = Auditorium
        fields = ['name', 'image', 'address', 'postalCode', 'city', 'province', 'capacity']
