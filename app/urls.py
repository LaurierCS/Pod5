from django.urls import path
from . import views

urlpatterns = [
    # Page Urls
    path('', views.homepage, name='index'),
    path('login', views.loginView, name = 'login'),
    path('register', views.register, name = 'register'),
    path('notes',views.notes, name='notes'),
    path('homepage',views.homepage, name='homepage'),
    path('settings',views.settings, name='settings'),
    path('account',views.account, name='account'),
    path('progress',views.progress, name='progress'),

    # Task Urls
    path('add',views.addTodo,name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete',views.deleteCompleted, name='deletecomplete'),
    path('deleteall',views.deleteAll,name='deleteall'),
]
