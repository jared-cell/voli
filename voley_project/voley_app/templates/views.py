# voley_app/views.py (Código Python correcto)

from django.shortcuts import render

def inicio_view(request):
    # Asegúrate de usar la ruta completa a la plantilla
    return render(request, 'voley_app/inicio.html', {})

def login_view(request): 
    # Asegúrate de usar la ruta completa a la plantilla
    return render(request, 'voley_app/login.html', {})