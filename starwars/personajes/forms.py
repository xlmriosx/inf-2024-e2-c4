from django import forms
from .models import Personaje

class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        # fields = ['alias', 'nombre_completo', 'casa', 'tiempo', 'foto']
        fields = '__all__'
