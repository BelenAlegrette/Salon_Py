from django.urls import reverse_lazy
from django.views import View


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView


from .models import Evento

# Create your views here.

#EVENTOS
class EventoBaseView(View):
    template_name = 'salon.html'
    model = Evento
    fields = '__all__'
    success_url = reverse_lazy('evento:all')


class EventoListView(EventoBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS EVENTOS
    """

class EventoDetailView(EventoBaseView,DetailView):
    template_name = "evento_detail.html"

class EventoCreateView(EventoBaseView,CreateView):
    template_name = "evento_create.html"
    extra_context = {
        "tipo": "Crear evento"
    }

class EventoUpdateView(EventoBaseView,UpdateView):
    template_name = "evento_create.html"
    extra_context = {
        "tipo": "Actualizar evento"
    }

class EventoDeleteView(EventoBaseView,DeleteView):
    template_name = "evento_delete.html"
    extra_context = {
        "tipo": "Borrar evento"
    }
   
