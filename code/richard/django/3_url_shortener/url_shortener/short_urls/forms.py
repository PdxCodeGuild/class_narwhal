from .models import Shortcode
from django import forms

class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model = Shortcode
        fields = ['url_long']

        widgets = {
            'url_long': forms.TextInput()
        }
