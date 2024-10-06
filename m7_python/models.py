
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    rut = models.CharField(max_length=12, blank=True, null=True)
    rol = models.CharField(max_length=50, choices=[('dueño', 'Dueño'), ('cliente', 'Cliente')], default='cliente')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def is_dueño(self):
        return self.rol == 'dueño'


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

class CustomUser(AbstractUser):
    role = models.CharField(max_length=12, choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador')])
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    
class Solicitud(models.Model):
    arrendatario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'arrendatario'})
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('aprobada', 'Aprobada'), ('rechazada', 'Rechazada')], default='pendiente')

    def __str__(self):
        return f"Solicitud de {self.arrendatario.username} para {self.inmueble.nombre}"