from django.db import models

# Create your models here.

class Pelicula(models.Model): 

    titulo = models.TextField(max_length = 30)
    genero = models.TextField(max_length = 20)
    precio = models.FloatField()
    duracion = models.IntegerField()
   
class User(models.Model): 

    nombre = models.TextField(max_length = 50)
    mail =   models.EmailField()
    localidad = models.TextField(max_length = 50)
