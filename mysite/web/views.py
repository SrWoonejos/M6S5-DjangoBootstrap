from django.shortcuts import render

def index(request):
    return render(request, 'web/index.html')  # Renderiza la plantilla 'index.html'

def navbar(request):
    return render(request, 'web/navbar.html')  # Renderiza la plantilla 'navbar.html'