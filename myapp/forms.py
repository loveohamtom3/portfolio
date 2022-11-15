from django import forms
from .models import Restaurants


class SearchForm(forms.Form):
     class Meta:
      model = Restaurants
      fields = ('name','address','description','menu')

     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
