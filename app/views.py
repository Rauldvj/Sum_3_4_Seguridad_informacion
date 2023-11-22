from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .forms import RegistroUsuarioForm
from personal.models import UsuarioPersonalizado
from django.contrib.auth import login as auth_login
 
# Create your views here.
 
def login(request):
    return render(request, 'registration/login.html')
 
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/registro.html', {'form': form})