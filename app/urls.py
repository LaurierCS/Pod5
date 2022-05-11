from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginpage, name ='login'),
    path('', views.homepage, name='index'),
    path('add',views.addTodo,name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete',views.deleteCompleted, name='deletecomplete'),
    path('deleteall',views.deleteAll,name='deleteall')
]
