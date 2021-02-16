from django.test import TestCase
from django.urls import reverse

from grados.models import Grado
from empleados.models import Empleado
from roles.models import Rol

# Create your tests here.

class TestGradoModelo(TestCase):
    
    def setUp(self):
        
        self.grado = Grado.objects.create(
            jornada = 'Mañana',
            empleados = Empleado.objects.create(
                            jornada = 'Mañana',
                            roles = Rol.objects.create(rol='Docente'),
                            nombre_completo = 'Jorge Umaña',
                            edad = 25,
                            cedula = '123456',
                            email = 'hola@hola.com'
                        ),
            nombre_grado = '1er Grado'            
        )

        
    def test_str_modelo(self):
        self.assertEqual(str(self.grado), f"Grado 1er Grado del empleado Jorge Umaña")
        
class TestGradoVistas(TestCase):
      
    def test_obtener_lista_empleados_status_code(self):
        peticion = self.client.get(reverse('grados:lista'))
        self.assertEqual(peticion.status_code, 200)