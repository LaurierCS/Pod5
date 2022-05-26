# Imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# User Login Form:
class User_Registration(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User # built in form for user handling
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    #input validation:
    def save(self, commit=True):
        user = super(User_Registration, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

class TodoForm(forms.Form):
    title = forms.CharField()

    class Meta:
        model = Todo
        fields = ['title']

    def save(self, commit = True):
        task = super(TodoForm, self).save(commit = False)
        task.title = self.cleaned_data['title']
        if commit:
            task.save()
        return task


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter task here', 'aria-label': 'Todo', 'aria-describedby': 'add-btn'}))
