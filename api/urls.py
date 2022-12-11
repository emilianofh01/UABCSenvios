from django.urls import path, include
from rest_framework import routers
from api.viewsets import *


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'dron', DroneViewSet)

urlpatterns = [
    path('', include(router.urls)),
]