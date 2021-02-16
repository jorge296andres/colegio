from django.urls import path

from empleados.views import CrearEmpleado
from empleados.views import EditarEmpleado
from empleados.views import EliminarEmpleado
from empleados.views import ListaEmpleado
from empleados.views import Inicio

app_name = 'empleados'
urlpatterns = [
    path('empleado/crear/', CrearEmpleado.as_view(), name='crear'),
    path('empleado/editar/<int:pk>/', EditarEmpleado.as_view(), name='editar'),
    path('empleado/eliminar/<int:pk>/', EliminarEmpleado.as_view(), name='eliminar'),
    path('empleados/lista', ListaEmpleado.as_view(), name='lista'),
    path('', Inicio.as_view(), name='inicio'),
]