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