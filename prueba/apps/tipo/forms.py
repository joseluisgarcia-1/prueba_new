from django import forms
from apps.tipo.models import Objetivos, Pedido

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

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = [
        ]
