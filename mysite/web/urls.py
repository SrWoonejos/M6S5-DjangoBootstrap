from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para el inicio
    path('navbar/', views.navbar, name='navbar'),  # Ruta para la barra de navegación
]