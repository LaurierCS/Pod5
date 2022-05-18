import re
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import *
from .models import Todo


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

def index (request):
    todo_list = Todo.object.order_by('id')

    form = TodoForm()

    context = {'todo_list':todo_list, 'form,':form}

    template_name = "app/homepage.html"
    return render(request, template_name, context)

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