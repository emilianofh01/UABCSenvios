from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request, 'app/index.html')

def servicio(request): 
    return render(request, 'app/servicios.html')

def acerca(request): 
    return render(request, 'app/acerca.html')

def contacto(request): 
    return render(request, 'app/contacto.html')