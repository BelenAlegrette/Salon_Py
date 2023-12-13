from django.db import models

# Create your models here.
from django.db.models import Model

  
    
    # podemos crear la tabla con un nombre especifico pero se lo tenemos
    # que indicar directamente en la metaclase


class Evento(Model):
    nombre = models.CharField(max_length=100, default="Evento sin nombre")
    descripcion = models.TextField(default="Descripción del evento")
    fecha = models.DateField(blank=False, null=False, auto_now=True)

    def __str__(self):
        return f"Evento: {self.nombre}, Descripción: {self.descripcion}, Fecha: {self.fecha}"
    class Meta:
       db_table = "salon_eventos"
