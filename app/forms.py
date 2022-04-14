# Imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# User Login Form:
class User_Login(forms.ModelForm):
    email = forms.EmailField(max_length=200, required=True)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100, required=True)

    class Meta:
        model = User
        fields = ('email', 'password') 