from django import forms
from apps.pedidos.models import Pedidos

class PedidosForm(forms.ModelForm):

    class Meta:
        model = Pedidos

        fields = [
            'fechauno',
            'objetivo',
            'tienda',
            'departamento',
            'vendedor',
            'producto',
            'valor',
            'fechados',
        ]

        labels = {
            'fechauno': 'Fecha toma de pedido',
            'objetivo': 'Objetivo',
            'tienda':'Tienda',
            'departamento':'Departamento',
            'vendedor':'Vendedor',
            'producto': 'Producto',
            'valor': 'Valor',
            'fechados':'Fecha de despacho',
        }

        widgets = {
            'fechauno': forms.DateTimeInput(attrs={'class':'form-control'}),
            'objetivo': forms.Select(attrs={'class:': 'form-control'}),
            'tienda': forms.Textarea(attrs={'class': 'form-control'}),
            'departamento': forms.Textarea(attrs={'class': 'form-control'}),
            'vendedor': forms.Textarea(attrs={'class': 'form-control'}),
            'producto': forms.Textarea(attrs={'class':'form-control'}),
            'valor': forms.TextInput(attrs={'class':'form-control'}),
            'fechados': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }
