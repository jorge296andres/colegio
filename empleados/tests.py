from django.test import TestCase
from django.urls import reverse

from empleados.models import Empleado
from roles.models import Rol

# Create your tests here.

class TestEmpleadoModelo(TestCase):
    
    def setUp(self):
        
        self.empleado = Empleado.objects.create(
            jornada = 'Mañana',
            roles = Rol.objects.create(rol='Docente'),
            nombre_completo = 'Jorge Umaña',
            edad = 25,
            cedula = '123456',
            email = 'hola@hola.com'
        )

        
    def test_str_modelo(self):
        self.assertEqual(str(self.empleado), 'Jorge Umaña')
        
class TestEmpleadoVistas(TestCase):
      
    def test_obtener_lista_empleados_status_code(self):
        peticion = self.client.get(reverse('empleados:lista'))
        self.assertEqual(peticion.status_code, 200)