from django.shortcuts import render
from .forms import UserLoginForm 
# Create your views here.
def index(request): 
    return render(request, 'app/index.html')

def servicio(request): 
    return render(request, 'app/servicios.html')

def acerca(request): 
    return render(request, 'app/acerca.html')

def contacto(request): 
    return render(request, 'app/contacto.html')

def login(request):
    form= UserLoginForm()
    ctx={'form':form}
    return render(request, 'app/login.html',ctx)

    