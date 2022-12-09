from django.urls import path
from . import views
from .forms import UserLoginForm
from django.contrib.auth.views import LoginView

urlpatterns = [
    
    path('', views.index, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    path('servicios/', views.servicio, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login, name='login_user'),

]