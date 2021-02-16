from django.db import models

from empleados.models import Empleado

# Create your models here.
class Grado(models.Model):
    MANANA = 'mañana'
    TARDE = 'tarde'
    HORARIOS = [
        (MANANA, 'Mañana'),
        (TARDE, 'Tarde'),
    ]
    
    jornada = models.CharField(max_length=6, choices=HORARIOS, default=MANANA)
    
    empleados = models.ForeignKey(Empleado, related_name='grados', on_delete=models.CASCADE)
    nombre_grado = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Grados'
        
    def __str__(self):
        return f"Grado {self.nombre_grado} del empleado {self.empleados.nombre_completo}"