from django.apps import AppConfig
from django.contrib import admin

class M7PythonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'm7_python'

    def ready(self):
       
        from .models import CustomUser, Inmueble, Region, Comuna, Solicitud
        
       
        admin.site.register(CustomUser)
        admin.site.register(Inmueble)
        admin.site.register(Region)
        admin.site.register(Comuna)
        admin.site.register(Solicitud)
