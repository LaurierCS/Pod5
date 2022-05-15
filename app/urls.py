from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage, name='index'),
    path('add',views.addTodo,name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete',views.deleteCompleted, name='deletecomplete'),
    path('deleteall',views.deleteAll,name='deleteall'),
    path('notes',views.notes, name='notes'),
    path('homepage',views.homepage, name='homepage'),
    path('settings',views.settings, name='settings'),
    path('account',views.account, name='account'),
]
