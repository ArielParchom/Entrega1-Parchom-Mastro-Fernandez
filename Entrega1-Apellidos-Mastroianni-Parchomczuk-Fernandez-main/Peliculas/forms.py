from django import forms
from Peliculas.models import Pelicula

class FormularioPelicula(forms.Form):
    titulo = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=20)
    precio = forms.FloatField()
    duracion = forms.IntegerField()

class FomularioBusqueda(forms.Form):
    titulo = forms.CharField(max_length=50, required=False)

