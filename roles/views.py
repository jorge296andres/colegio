from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from roles.models import Rol
from roles.forms import RolForm

# Create your views here.
class CrearRol(CreateView):
    form_class = RolForm
    success_url = reverse_lazy('roles:lista')
    template_name = 'roles/crear.html'

class EditarRol(UpdateView):
    model = Rol
    form_class = RolForm
    success_url = reverse_lazy('roles:lista')
    template_name = 'roles/editar.html'
    
class EliminarRol(DeleteView):
    model = Rol
    success_url = reverse_lazy('roles:lista')
    template_name = 'roles/eliminar.html'

class ListaRoles(ListView):
    model = Rol
    context_object_name = 'roles'
    template_name = 'roles/lista.html'