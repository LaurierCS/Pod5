from django.urls import path
from . import views

urlpatterns = [
    path('auth', views.authentication, name='auth'),
    path('login', views.loginpage, name ='login'),
    path('', views.homepage, name='index'),
    
]
