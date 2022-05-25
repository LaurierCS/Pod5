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
    path('upload', views.taskPost, name = 'upload'),
    path('todo', todoView.as_view()),
]
