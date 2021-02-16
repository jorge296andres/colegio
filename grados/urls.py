from django.urls import path

from grados.views import CrearGrado
from grados.views import EditarGrado
from grados.views import EliminarGrado
from grados.views import ListaGrados

app_name = 'grados'
urlpatterns = [
    path('crear/', CrearGrado.as_view(), name='crear'),
    path('editar/<int:pk>/', EditarGrado.as_view(), name='editar'),
    path('eliminar/<int:pk>/', EliminarGrado.as_view(), name='eliminar'),
    path('lista/', ListaGrados.as_view(), name='lista'),
]