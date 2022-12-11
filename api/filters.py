from django_filters  import rest_framework as filters
from app.models import *

class DronesFilter(filters.FilterSet):
    class Meta:
        model = Dron
        fields = {
            'nombre': ['icontains'],
            'inventario': ['gt', 'lt'],
            'peso_maximo': ['gt', 'lt', 'gte', 'lte'],
            'velocidad': ['gt', 'lt', 'gte', 'lte'],
        }