from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    path('servicios/', views.servicio, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
]