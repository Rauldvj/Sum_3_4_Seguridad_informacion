from django.contrib.auth.models import AbstractUser
from django.db import models
from .opciones import *


# Create your models here.

# Estos campos definen la estructura de la base de datos para almacenar información relacionada con personas, como sus nombres, apellidos, dirección, teléfono y RUT.

class Persona(models.Model):
    rut = models.CharField(max_length=10, unique=True, verbose_name='Rut')
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    direccion = models.CharField(max_length=100, verbose_name='Dirección')
    telefono = models.CharField(max_length=10, verbose_name='Teléfono')


    # Se indica que la clase que contiene esta metaclase es abstracta y no debe generar una tabla en la base de datos.
    
    class Meta:
        abstract = True

# Esta clase modela a un bombero, extendiendo la clase Persona y añadiendo un campo adicional rango para representar el rango específico del bombero.

class Bombero(Persona):
    rango = models.CharField(max_length=20, choices=opciones_rango, verbose_name='Rango')

    # La implementación devuelve una cadena que combina el valor del atributo rango, nombres, y apellido_paterno.
    
    def __str__(self):
        return f'{self.rango} {self.nombres} {self.apellido_paterno}'
    

class UsuarioPersonalizado(AbstractUser):
    rut = models.CharField(max_length=10, unique=True, verbose_name='Rut')
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    direccion = models.CharField(max_length=100, verbose_name='Dirección')
    telefono = models.CharField(max_length=10, verbose_name='Teléfono')
    rango = models.CharField(max_length=20, choices=opciones_rango, verbose_name='Rango')