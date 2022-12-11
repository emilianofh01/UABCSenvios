from django.db import models
from datetime import datetime
from django.conf import settings
# Create your models here.
class Momento(models.Model):
    title= models.CharField(max_length=200)
    content = models.TextField
    create_at= models.DateTimeField(default=datetime.now, blank=True)
    lat= models.DecimalField (max_digits=18, decimal_places=14, blank=True)
    lon= models.DecimalField (max_digits=18, decimal_places=14, blank=True)
    user_id= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Dron(models.Model):
    inventario=models.IntegerField()
    velocidad=models.FloatField()
    nombre=models.CharField(max_length=120)
    desc=models.CharField(max_length=3200)
    peso_maximo=models.FloatField()
    icono=models.CharField(max_length=120)

class Envio(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lat_inicio = models.FloatField()
    lon_inicio = models.FloatField()
    hora_inicio = models.DateTimeField()
    lat_fin = models.FloatField()
    lon_fin = models.FloatField()
    hora_fin = models.DateTimeField()
    dron = models.ForeignKey(Dron, on_delete=models.CASCADE)
