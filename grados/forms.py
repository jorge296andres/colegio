from django import forms

from empleados.models import Empleado

from grados.models import Grado

class GradoForm(forms.ModelForm):
    jornada = forms.Select(choices=Grado.HORARIOS)
    
    nombre_grado = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'input', 'placeholder': '1er Grado, 2do Grado...'}))
    
    empleados = forms.ModelChoiceField(queryset=Empleado.objects.all())
    
    class Meta:
        model = Grado
        fields = ('jornada', 'empleados', 'nombre_grado',)
    
    def clean_empleados(self):
        empleado = self.cleaned_data['empleados']
        jornada_grado = self.cleaned_data['jornada']
        
        if not empleado.jornada.lower() == jornada_grado.lower():
            raise forms.ValidationError('Horario no permitido para titular')
        print(empleado)
        return empleado