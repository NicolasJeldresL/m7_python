from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile
from django.contrib.auth.views import LoginView

# Formulario para el registro de usuarios
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Formulario para editar el perfil del usuario
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Formulario para editar o añadir datos del perfil del usuario (UserProfile)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['rol', 'direccion', 'telefono', 'rut', 'avatar', 'bio']


# Vista personalizada para el login (si necesitas personalizarla)
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
