from re import L
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST
from django.views import View, generic

from .forms import *
from .models import Todo
from .models import *

"""
Page Views
"""
# Index
def homepage(request):
    task = Todo()
    form = TodoForm()

    context = {'task':task, 'form':form}
    template_name = "app/homepage.html"

    return render(request, template_name, context)

# Register Handler
def register(request):
    if request.method == "POST":
        user_form = User_Registration(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            messages.success(request, "Registration successful." )
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    else:
        user_form = User_Registration()

    context = {"register_form": user_form}

    return render(request, "app/login/register.html", context)

# Login Handler
def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
    
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
    
            if user is not None:
                login(request, user)
                messages.info(request, "you are logged in as {username}")
                return redirect("index")
    
            else:
                messages.info(request, "Username or password is incorrect")
    
        else:
            messages.info(request, "Invalid username or password.")
    
    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "app/login/login.html", context)

# Page Handlers
def notes(request):
    return render(request, 'app/notes.html')

def homepage(request):
    return render(request, 'app/homepage.html')

def settings(request):
    return render(request, 'app/settings.html')

def account(request):
    return render(request, 'app/login/login.html')

def progress(request):
    return render(request, 'app/progress.html')


"""
Task Views
"""
# Create Task
def taskPost(request):
    if request.POST:
        taskForm = TodoForm(request.POST)
        if taskForm.is_valid():
            taskForm.save()
        return redirect("index")
    return render(request, 'app/todo/task_upload.html', {'form': taskForm})

class todoView(generic.ListView):
    model = Todo
    template_name = "app/todo/todo.html"