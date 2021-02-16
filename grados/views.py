from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from grados.models import Grado
from grados.forms import GradoForm

# Create your views here.
class CrearGrado(CreateView):
    form_class = GradoForm
    success_url = reverse_lazy('grados:lista')
    template_name = 'grados/crear.html'

class EditarGrado(UpdateView):
    model = Grado
    form_class = GradoForm
    success_url = reverse_lazy('grados:lista')
    template_name = 'grados/editar.html'

class EliminarGrado(DeleteView):
    model = Grado
    success_url = reverse_lazy('grados:lista')
    template_name = 'grados/eliminar.html'

class ListaGrados(ListView):
    model = Grado
    context_object_name = 'grados'
    template_name = 'grados/lista.html'