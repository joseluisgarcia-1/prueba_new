from django.db import models
from numpy import product
from apps.tipo.models import Descripcion


class Pedidos(models.Model):
    fechauno = models.CharField(max_length = 5000000)
    objetivo = models.ForeignKey(Descripcion, null=True, blank=True, on_delete=models.CASCADE)
    tienda = models.CharField(max_length = 5000000)
    departamento = models.CharField(max_length = 5000000)
    vendedor = models.CharField(max_length = 5000000)
    producto = models.CharField(max_length = 5000000)
    valor = models.CharField(max_length = 5000000)
    fechados = models.CharField(max_length = 5000000)
