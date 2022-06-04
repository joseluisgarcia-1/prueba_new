from django.db import models
from numpy import product
from apps.tipo.models import Objetivos


class Pedidos(models.Model):
    fechauno = models.DateField()
    objetivo = models.ForeignKey(Objetivos, null=True, blank=True, on_delete=models.CASCADE)
    tienda = models.CharField(max_length = 500)
    departamento = models.CharField(max_length = 500)
    vendedor = models.CharField(max_length = 200)
    producto = models.CharField(max_length = 5000000)
    valor = models.IntegerField()
    fechados = models.DateField()
