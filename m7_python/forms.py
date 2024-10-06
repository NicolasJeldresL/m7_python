from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile
from django.contrib.auth.views import LoginView
from .models import Inmueble
from django.contrib.auth.forms import UserCreationForm
from .models import Inmueble, Solicitud

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    rol = forms.ChoiceField(choices=[('dueño', 'Dueño'), ('cliente', 'Cliente')])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'rol']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['telefono', 'direccion', 'bio', 'rut', 'rol', 'avatar']
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'direccion', 'precio', 'disponible', 'comuna', 'arrendador']

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'precio', 'comuna', 'disponible']

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['inmueble', 'estado']
        