from django.shortcuts import render
from .forms import UserLoginForm 
from .forms import UserRegister
from django.contrib import messages
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

def register(request):
    formu= UserRegister()
    if request.method=='POST':
        formu= UserRegister(request.POST)
        if formu.is_valid:
            formu.save()
            messages.success(request, 'Datos almacenados correctamente')
    ctx={'formu':formu}
    return render(request, 'app/register.html',ctx)
    