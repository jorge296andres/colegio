from django.db import models

# Create your models here.
class Rol(models.Model):
    rol = models.CharField(max_length=25)
    
    class Meta:
        verbose_name_plural = 'Roles'
        
    def __str__(self):
        return self.rol