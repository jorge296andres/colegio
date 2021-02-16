from django.test import TestCase
from django.urls import reverse

from roles.models import Rol

# Create your tests here.
class TestRolModelo(TestCase):
    
    def setUp(self):
        self.rol = Rol.objects.create(rol='Docente')
        
    def test_str_modelo(self):
        self.assertEqual(str(self.rol), 'Docente')
        
class TestRolVistas(TestCase):
    
    def test_crear_rol(self):
        self.client.post(reverse('roles:crear'), {'rol': 'Director'})
        self.assertEqual(Rol.objects.first().rol, 'Director')
        
    def test_obtener_lista_roles_status_code(self):
        peticion = self.client.get(reverse('roles:lista'))
        self.assertEqual(peticion.status_code, 200)