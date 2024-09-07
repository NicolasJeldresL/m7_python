# aquí van nuestros Formularios
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile

#TODO_ REGISTER - FORM

class CustomUserCreationForm(UserCreationForm):
    # -> Model User
    pass

#TODO_ REGISTER_ROL - FORM  +  Etapa de Edit PROFILE
class UserProfileForm(forms.ModelForm):
    # -> Model UserProfile
    pass


#TODO_ EDIT PROFILE -FORM
