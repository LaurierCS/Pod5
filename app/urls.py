from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('notes',views.notes, name='notes'),
    path('homepage',views.homepage, name='homepage'),
    path('settings',views.settings, name='settings'),
    path('account',views.account, name='account'),
]
