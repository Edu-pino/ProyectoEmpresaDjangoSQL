from django.urls import path, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Url de la página de login.
    path('', views.loginView, name='loginView'),
    path('landing', views.landingView, name='landingView'),
    path('salir/', views.logoutView, name='logoutView'),
    path('get_data/', views.get_data, name='get_data')
    
    
    
]