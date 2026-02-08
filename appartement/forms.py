from django import forms
from .models import Appartement

class AppartementForm(forms.ModelForm):
    class Meta:
        model = Appartement
        fields = '__all__'
