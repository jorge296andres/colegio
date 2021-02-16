from django import forms

from roles.models import Rol

class RolForm(forms.ModelForm):
    rol = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'input', 'placeholder': 'Docente Historia, Docente Inglés...'}))
    
    class Meta:
        model = Rol
        fields = ('rol',)