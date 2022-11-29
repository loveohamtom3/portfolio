from django import forms


class SearchForm(forms.Form):
    Name = forms.CharField(label='店名',max_length=200,required=True)
    
