from api.serializers import *
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets
from app.models import Dron
from api.filters import DronesFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(methods=['get'], detail=False)
    def current(self, request):
        serializer = self.get_serializer_class()(request.user)
        return Response(serializer.data)

class DronViewSet(viewsets.ModelViewSet):
    queryset = Dron.objects.all()
    filterset_class = DronesFilter
    serializer_class = DronSerializer

    
class EnvioViewSet(viewsets.ModelViewSet):
    queryset = Envio.objects.all()
    #filterset_class = DronesFilter
    serializer_class = EnvioSerializer