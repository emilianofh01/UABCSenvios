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
        fields = [
            'inventario',
            'velocidad',
            'nombre',
            'desc',
            'peso_maximo',
            'precio',
            'icono',
            'id',
            'url'
        ]
        
class EnvioSerializer(serializers.HyperlinkedModelSerializer):
    dron_id = serializers.PrimaryKeyRelatedField(many=False, read_only=False,queryset=Dron.objects.all())
    user_id = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Envio
        fields = [ 'user_id', 'dron_id', 'lat_inicio', 'lon_inicio', 'hora_inicio', 'lat_fin', 'lon_fin', 'hora_fin']
    
    def create(self, validated_data):
        validated_data['dron']=validated_data.pop('dron_id')
        validated_data['user_id'] = self.context['request'].user
        return Envio.objects.create(**validated_data)