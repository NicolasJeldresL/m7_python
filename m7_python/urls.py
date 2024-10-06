from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),  
    path('login/', auth_views.LoginView.as_view(), name='login'), 
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.agregar_usuario, name='agregar_usuario'),  
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('inmueble/nuevo/', views.agregar_inmueble, name='agregar_inmueble'),
    path('inmueble/<int:id>/editar/', views.editar_inmueble, name='editar_inmueble'),
    path('inmueble/<int:inmueble_id>/eliminar/', views.eliminar_inmueble, name='eliminar_inmueble'),  
    path('inmuebles/', views.listar_inmuebles, name='listar_inmuebles'),
    path('solicitar-arriendo/<int:inmueble_id>/', views.solicitar_arriendo, name='solicitar_arriendo'),
    path('gestionar-solicitudes/', views.gestionar_solicitudes, name='gestionar_solicitudes'),
]