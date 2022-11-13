from .models import Restaurants
from django import forms

class RestaurantsSearchForm(forms.Form):

    name = forms. CharField(
        initial='',
        label='店名',
        required = False, 
    )
    address= forms.CharField(
        initial='',
        label='住所',
        required=False,  
    )
    
    description= forms.CharField(
        initial='',
        label='説明',
        required=False,  
    )
    
    menu=forms.CharField(
       initial='',
        label='メニュー',
        required=False,  
    )