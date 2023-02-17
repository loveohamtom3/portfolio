from django import forms
from .models import User, Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SearchForm(forms.Form):
    Name = forms.CharField(label='店名',max_length=200,required=True)
    
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class ReviewForm(forms.ModelForm):   
    class Meta:
        model = Review
        fields = ['score', 'comment']
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email",)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'