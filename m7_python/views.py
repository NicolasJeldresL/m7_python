from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .services import get_all_inmuebles

# Create your views here.
def indexView(request):
    inmuebles = get_all_inmuebles()
    return render(request,'index.html',{'inmuebles':inmuebles} )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('index')  # Redirect to the home page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
