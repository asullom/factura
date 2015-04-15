from django.db import models

# Create your models here.


class Cliente(models.Model):

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre

    def hola(self):
        return "Hola %s" % self.nombre
