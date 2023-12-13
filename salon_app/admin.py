from django.contrib import admin
from django.contrib.admin import ModelAdmin


from .models import  Evento



@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha')

""" @admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'evento', 'fecha') """