from django import forms
from .models import Restaurants

class RestaurantsForm(forms.ModelForm):
   class Meta:
        model = Restaurants
        fields = ('Name', 'Address', 'Description', 'Menu')
class SearchForm(forms.Form):
    search_key = forms.CharField(
            label='',
            max_length=128,
            widget=forms.TextInput(attrs={"class": 'float-right', 'placeholder': 'Search...'}), required=False)