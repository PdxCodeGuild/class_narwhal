from django import forms
from .models import Grocery_Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Grocery_Item
        fields = ['description', 'date_created', 'date_completed', 'completed'  ]


