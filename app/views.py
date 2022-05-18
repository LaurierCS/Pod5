from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


def homepage(request):
    sentence = "Hakuna Matata"
    context = {
        "sentence": sentence,
    }
    template_name = "app/homepage.html"

    return render(request, template_name, context)

def loginpage(request):
    
    template_name = "app/loginpage.html"

    return render(request, template_name)

def notes(request):
    return render(request, 'app/notes.html')

def homepage(request):
    return render(request, 'app/homepage.html')

def settings(request):
    return render(request, 'app/settings.html')

def account(request):
    return render(request, 'app/signup.html')