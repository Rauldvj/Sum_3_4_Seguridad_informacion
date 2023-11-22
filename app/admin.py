from django.contrib import admin
from .models import *
from .models import UsuarioPersonalizado
# Register your models here.

class InventarioAdmin(admin.ModelAdmin):
    
    # Esta lista define los campos que se mostrarán en la interfaz de administración cuando se visualice la lista de objetos de algún modelo que incluya fechas, personas, carros y elementos.

    list_display = ('fecha', 'fecha_entrega', 'fecha_revision', 'realizado_por', 'revisado_por', 'carro', 'elemento')

    # Define el orden de visualización de los campos en el formulario de adición
    
    fields = ('fecha', 'fecha_entrega', 'fecha_revision', 'realizado_por', 'revisado_por', 'carro', 'elemento', 'marca', 'observaciones', 'cantidad', 'estado')

admin.site.register(Inventario, InventarioAdmin)

admin.site.register(UsuarioPersonalizado)