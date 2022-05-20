from django.urls import path
from . import views

urlpatterns = [

    # Page Urls
    path('', views.homepage, name='index'),
    path('login', views.loginView, name = 'login'),
    path('register', views.register, name = 'register'),

    # Task Urls
    path('add',views.addTodo,name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete',views.deleteCompleted, name='deletecomplete'),
    path('deleteall',views.deleteAll,name='deleteall')
]
