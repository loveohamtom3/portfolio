from django import forms
from .models import Name, Address

class SearchForm(forms.Form):
    selected_name = forms.ModelChoiceField(
        label='店名',
        required=False,
        queryset=Name.objects,
    )
    selected_address = forms.ModelChoiceField(
        label='住所',
        required=False,
        queryset=Address.objects,
    )
    freeword = forms.CharField(min_length = 2, max_length = 100, label='', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        selected_name = self.fields['selected_name']
        selected_address = self.fields['selected_address']