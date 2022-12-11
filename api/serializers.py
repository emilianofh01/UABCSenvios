from app.models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name']

        
class DronSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dron
        fields = '__all__'
        
class EnvioSerializer(serializers.HyperlinkedModelSerializer):
    dron_id = serializers.PrimaryKeyRelatedField(many=False, read_only=False,queryset=Dron.objects.all())
    class Meta:
        model = Envio
        fields = [ 'dron_id', 'lat_inicio', 'lon_inicio', 'hora_inicio', 'lat_fin', 'lon_fin', 'hora_fin']