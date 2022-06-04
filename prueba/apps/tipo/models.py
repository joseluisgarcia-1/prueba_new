from django.db import models

class Objetivos(models.Model):
    nombre = models.CharField(max_length=500000000)

    def __str__(self):
        return '{}'.format(self.nombre)

class Receta(models.Model):
    descripcion = models.ForeignKey(Objetivos, null=True, blank=True, on_delete=models.CASCADE)


