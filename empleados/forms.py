from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from empleados.models import Empleado
from roles.models import Rol

class EmpleadoForm(forms.ModelForm):
    jornada = forms.Select(choices=Empleado.HORARIOS)
    
    roles = forms.ModelChoiceField(queryset=Rol.objects.all())
    
    nombre_completo = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'input', 'placeholder': 'Jorge Umaña...'}))
    
    edad = forms.IntegerField(required=True, validators=[MinValueValidator(18), MaxValueValidator(110)],widget=forms.NumberInput(attrs={'class' : 'input', 'placeholder': '25'}))
    
    cedula = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'input', 'placeholder': '123123'}))
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class' : 'input', 'placeholder': 'hola@hola.com'}))
    
    class Meta:
        model = Empleado
        fields = ('jornada', 'roles', 'nombre_completo', 'edad', 'cedula', 'email',)