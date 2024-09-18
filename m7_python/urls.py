from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.indexView, name='index'),  
    path('login/', auth_views.LoginView.as_view(), name='login'), 
    #path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    #path('register/', views.register, name='agregar_usuario'),
    path('inmueble/nuevo/', views.agregar_inmueble, name='agregar_inmueble'),
    path('inmueble/<int:id>/editar/', views.editar_inmueble, name='editar_inmueble'),
    path('inmueble/<int:id>/eliminar/', views.eliminar_inmueble, name='eliminar_inmueble'),
    path('inmuebles/', views.listar_inmuebles, name='listar_inmuebles'),
    path('logout/', views.logout_view, name='logout'),
]
