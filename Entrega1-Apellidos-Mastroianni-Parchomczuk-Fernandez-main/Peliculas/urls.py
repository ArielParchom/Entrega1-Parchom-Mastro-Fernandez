from django.contrib import admin
from django.urls import path
from Peliculas import views 

urlpatterns = [
    path('', views.index, name = 'inicio'),
    path('catalogo', views.ver_catalogo, name = 'catalogo'),
    path('registrar-pelicula', views.registrar_pelicula, name = 'registrar-pelicula')
]