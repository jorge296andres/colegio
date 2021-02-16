from django.db import models

from roles.models import Rol

# Create your models here.
class Empleado(models.Model):
    MANANA = 'mañana'
    TARDE = 'tarde'
    HORARIOS = [
        (MANANA, 'Mañana'),
        (TARDE, 'Tarde'),
    ]
    
    jornada = models.CharField(max_length=6, choices=HORARIOS, default=MANANA)
        
    roles = models.ForeignKey(Rol, related_name='empleados', on_delete=models.CASCADE)
    
    nombre_completo = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField()
    cedula = models.CharField(max_length=20)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Empleados'
        
    def __str__(self):
        return self.nombre_completo