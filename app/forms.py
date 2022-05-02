# Imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
import requests


# Notion Form Setup:
class User_Notion_Setup():
    token = forms.CharField(max_length=50, required = True) # integration token
    databaseID = forms.CharField(max_length=32, required = True) # database id: url snippet
    
    class Meta:
        model = Notion_DB
        fields = ('token', 'databaseID')

    def save(self, commit = True):
        pass

# User Login Form:
class User_Login(forms.ModelForm):
    email = forms.EmailField(max_length=200, required=True)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100, required=True)

    class Meta:
        model = User
        fields = ('email', 'password') 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
       

class EditProfileForm(forms.ModelForm):
    username = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email')


