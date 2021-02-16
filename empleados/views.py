from django.urls import reverse_lazy

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from empleados.models import Empleado
from empleados.forms import EmpleadoForm

# Create your views here.
class CrearEmpleado(CreateView):
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados:lista')
    template_name = 'empleados/crear.html'

class EditarEmpleado(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados:lista')
    template_name = 'empleados/editar.html'

class EliminarEmpleado(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados:lista')
    template_name = 'empleados/eliminar.html'

class ListaEmpleado(ListView):
    model = Empleado
    context_object_name = 'empleados'
    template_name = 'empleados/lista.html'
    
class Inicio(TemplateView):
    template_name = 'inicio.html'