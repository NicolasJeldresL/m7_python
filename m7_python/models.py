# m7_python/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    rol = models.CharField(max_length=20, choices=(('arrendador', 'Arrendador'), ('arrendatario', 'Arrendatario')))
    rut = models.CharField(max_length=12, unique=True)


class Region(models.Model):
    cod = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    cod = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Inmueble(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default="Sin descripción")
    disponible = models.BooleanField(default=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    arrendador = models.ForeignKey(User, on_delete=models.CASCADE)
    m2_construidos = models.FloatField(null=True, blank=True)
    m2_totales = models.FloatField(null=True, blank=True)
    num_estacionamientos = models.IntegerField(null=True, blank=True)
    num_habitaciones = models.IntegerField(null=True, blank=True)
    num_baños = models.IntegerField(null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    tipo_inmueble = models.CharField(max_length=50, null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    precio_ufs = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nombre
