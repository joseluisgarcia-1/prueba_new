from django import forms
from apps.tipo.models import Objetivos, Receta

class ObjetivosForm(forms.ModelForm):

    class Meta:
        model = Objetivos
        fields = [
            'nombre',

        ]
        labels = {
            'nombre': 'Objetivos',
        }
        widgets = {
        }

class RecetaForm(forms.ModelForm):

    class Meta:
        model = Receta
        fields = [
        ]
