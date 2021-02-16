from django.urls import path

from roles.views import CrearRol
from roles.views import EditarRol
from roles.views import EliminarRol
from roles.views import ListaRoles

app_name = 'roles'
urlpatterns = [
    path('crear/', CrearRol.as_view(), name='crear'),
    path('editar/<int:pk>/', EditarRol.as_view(), name='editar'),
    path('eliminar/<int:pk>/', EliminarRol.as_view(), name='eliminar'),
    path('lista/', ListaRoles.as_view(), name='lista'),
]
