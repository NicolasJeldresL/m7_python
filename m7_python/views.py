from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .services import get_all_inmuebles
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth import login as auth_login
from .forms import InmuebleForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from .models import Inmueble

# Create your views here.
def indexView(request):
    inmuebles = get_all_inmuebles()
    return render(request, 'index.html', {'inmuebles': inmuebles})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
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

def eliminar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    if request.method == 'POST':
        inmueble.delete()
        return HttpResponseRedirect(reverse('listar_inmuebles'))
    return render(request, 'eliminar_inmueble.html', {'inmueble': inmueble})

def listar_inmuebles(request):
    inmuebles = Inmueble.objects.filter(disponible=True)
    return render(request, 'listar_inmuebles.html', {'inmuebles': inmuebles})

def logout_view(request):
    logout(request)
    return redirect('index')  

def profile(request):
    return render(request, 'profile.html')