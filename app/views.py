from django.shortcuts import render
from .forms import UserLoginForm 
from .forms import UserRegister
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect,render
# Create your views here.
def index(request): 
    return render(request, 'app/index.html')

def servicio(request): 
    return render(request, 'app/servicios.html')

def acerca(request): 
    return render(request, 'app/acerca.html')

def contacto(request): 
    return render(request, 'app/contacto.html')

def panel(request):
    if request.user.is_authenticated: 
        return render(request, 'app/panel.html')
    return redirect('login_user')

def login_user(request):
    if request.user.is_authenticated:
        return redirect("panel")
    form= UserLoginForm()
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user= authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                print(form.data.values())
                return redirect('panel')
            else:
                messages.error(request, 'Usuario o contraseña no encontrados')


    ctx={'form':form}
    return render(request, 'app/login.html',ctx)

def register(request):
    if request.user.is_authenticated:
        return redirect("panel")
    formu= UserRegister()
    if request.method=='POST':
        formu= UserRegister(request.POST)
        if formu.is_valid():
            formu.save()
            messages.success(request, 'Datos almacenados correctamente')
    ctx={'formu':formu}
    return render(request, 'app/register.html',ctx)
    
    