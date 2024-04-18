from django.urls import path, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Url de la página de login.
    path('', views.loginView, name='loginView'),
    path('landing', views.landingView, name='landingView'),
    path('salir/', views.logoutView, name='logoutView'),
    path('get_data/', views.get_data, name='get_data'),
    path('get_data_consulta_articulos_precio/', views.get_data_consulta_articulos_precio, name='get_data_consulta_articulos_precio'),
    path('get_data_consulta_articulos/', views.get_data_consulta_articulos, name='get_data_consulta_articulos'),
    path('get_data_consulta_albaran/', views.get_data_consulta_albaran, name='get_data_consulta_albaran'),
    path('get_data_consulta_cabecera_albaran/', views.get_data_consulta_cabecera_albaran, name='get_data_consulta_cabecera_albaran'),
    path('get_data_oferta_cliente/', views.get_data_oferta_cliente, name='get_data_oferta_cliente'),
    path('get_data_modal/', views.get_data_modal, name='get_data_modal'),
    path('get_data_frontend/', views.get_data_frontend, name='get_data_frontend')



    
    
    
]