# voley_app/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


def inicio_view(request):
    # Renderiza la plantilla HTML de inicio
    return render(request, 'inicio.html', {})


def login_view(request):
    """Login simple: acepta POST con 'username' y 'password'."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('inicio')
        messages.error(request, 'Credenciales inválidas, inténtalo otra vez.')
        return render(request, 'login.html', {})

    return render(request, 'login.html', {})


def register_view(request):
    """Registro usando CustomUserCreationForm con email obligatorio."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('inicio')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def dashboard_view(request):
    """Renderiza el panel de control (dashboard)."""
    context = {
        'username': request.user.get_username()
    }
    return render(request, 'dashboard.html', context)


def logout_view(request):
    """Cierra la sesión del usuario y redirige al inicio."""
    if request.method == 'POST':
        identifier = request.POST.get('username')
        password = request.POST.get('password')
        # permitir login por email o username
        user = None
        if identifier and '@' in identifier:
            try:
                u = User.objects.get(email=identifier)
                user = authenticate(request, username=u.username, password=password)
            except User.DoesNotExist:
                user = None
        else:
            user = authenticate(request, username=identifier, password=password)