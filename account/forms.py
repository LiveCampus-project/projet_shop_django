from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ( 'email', 'last_name', 'first_name',  'password1', 'password2')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','last_name', 'first_name', 'password')