from re import L
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST

from .forms import *
from .models import Todo
from .models import *

# Index
def homepage(request):
    task = Todo()
    form = TodoForm()

    context = {'task':task, 'form':form}
    template_name = "app/homepage.html"

    return render(request, template_name, context)

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

# Task Methods:
@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo=Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completeTodo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')


def notes(request):
    return render(request, 'app/notes.html')

def homepage(request):
    return render(request, 'app/homepage.html')

def settings(request):
    return render(request, 'app/settings.html')

def account(request):
    return render(request, 'app/signup.html')

def progress(request):
    return render(request, 'app/progress.html')