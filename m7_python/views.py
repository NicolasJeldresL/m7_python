from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .services import get_all_inmuebles
from .forms import UserRegisterForm, UserUpdateForm, InmuebleForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from .models import Inmueble
from .forms import CustomUserCreationForm
from .models import UserProfile
from django.contrib.auth import login as auth_login
from .models import Inmueble, Comuna, Region, Solicitud
from .forms import InmuebleForm, SolicitudForm

def indexView(request):
    inmuebles = get_all_inmuebles()
    return render(request, 'index.html', {'inmuebles': inmuebles})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, rol=request.POST.get('rol'))
            auth_login(request, user)
        
            if user.userprofile.is_dueño():  
                return redirect('nombre_de_vista_dueño')  
            else:
                return redirect('nombre_de_vista_cliente')  
    else:
        form = UserRegisterForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'profile_edit.html', {'form': form})

def agregar_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inmuebles')  
    else:
        form = InmuebleForm()
    return render(request, 'agregar_inmueble.html', {'form': form})

def editar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('listar_inmuebles')
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, 'editar_inmueble.html', {'form': form})

@login_required
def eliminar_inmueble(request, inmueble_id):  
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        inmueble.delete() 
        return redirect('listar_inmuebles')  
    return render(request, 'eliminar_inmueble.html', {'inmueble': inmueble})

def listar_inmuebles(request):
    inmuebles = Inmueble.objects.filter(disponible=True)
    return render(request, 'listar_inmuebles.html', {'inmuebles': inmuebles})

def logout_view(request):
    logout(request)
    return redirect('index')  

def profile(request):
    return render(request, 'profile.html')

def agregar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect('listar_inmuebles')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def lista_inmuebles(request):
    region_id = request.GET.get('region')
    comuna_id = request.GET.get('comuna')

    inmuebles = Inmueble.objects.filter(disponible=True)
    regiones = Region.objects.all()

    if region_id:
        inmuebles = inmuebles.filter(comuna__region__id=region_id)
    if comuna_id:
        inmuebles = inmuebles.filter(comuna__id=comuna_id)

    return render(request, 'inmuebles/lista_inmuebles.html', {'inmuebles': inmuebles, 'regiones': regiones})


@login_required
def agregar_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.arrendador = request.user
            inmueble.save()
            return redirect('listar_inmuebles')
    else:
        form = InmuebleForm()
    return render(request, 'agregar_inmueble.html', {'form': form})


@login_required
def gestionar_solicitudes(request):
    solicitudes = Solicitud.objects.filter(inmueble__arrendador=request.user)
    return render(request, 'solicitudes/gestionar_solicitudes.html', {'solicitudes': solicitudes})


@login_required
def solicitar_arriendo(request, inmueble_id):
    inmueble = Inmueble.objects.get(id=inmueble_id)
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.arrendatario = request.user
            solicitud.inmueble = inmueble
            solicitud.save()
            return redirect('lista_inmuebles')
    else:
        form = SolicitudForm()
    return render(request, 'solicitudes/solicitar_arriendo.html', {'form': form, 'inmueble': inmueble})

    