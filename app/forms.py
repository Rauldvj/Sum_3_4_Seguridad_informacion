from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado

class CustomUserCreationForm(UserCreationForm):
    pass

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ('username', 'rut', 'nombres', 'apellido_paterno', 'apellido_materno', 'direccion', 'telefono', 'rango')