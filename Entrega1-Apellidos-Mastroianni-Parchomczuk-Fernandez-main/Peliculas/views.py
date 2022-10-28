from django.shortcuts import render, redirect
from Peliculas.models import Pelicula
from Peliculas.forms import FormularioPelicula, FomularioBusqueda
from datetime import datetime


def index(request): 
    return render(request, 'layouts/index.html', {'title' : 'inicio'})


def ver_catalogo(request): 

    cant_registros = Pelicula.objects.all().count()
    formulario = FomularioBusqueda()

    titulo = request.GET.get('titulo', None)
    if titulo: 
        pelicula = Pelicula.objects.filter(titulo__icontains = titulo)
    else: 
        pelicula = Pelicula.objects.all()
    
    return render(request, 'layouts/ver_catalogo.html', {'pelicula' : pelicula, 'cantidad' : cant_registros,  'form' : formulario})
    

def registrar_pelicula(request):

    if request.method == "POST":
        
        formulario = FormularioPelicula(request.POST)
        
        if formulario.is_valid():

            data = formulario.cleaned_data
                          
            pelicula = Pelicula(

                titulo = data['titulo']
                ,genero = data['genero']
                ,precio = data['precio']
                ,duracion = data['duracion']
            )
            pelicula.save()
            
            return redirect('catalogo')

    formulario = FormularioPelicula()  
    return render(request, 'layouts/registrar_pelicula.html', {'formulario' : formulario})
