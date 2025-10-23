# voley_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('voley_app.urls')), # <--- Incluye las URLs de voley_app
]