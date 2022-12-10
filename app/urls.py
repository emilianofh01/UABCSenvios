from django.urls import path
from . import views
from .forms import UserLoginForm
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register, name='register_user'),
    path('panel/', views.panel, name='panel'),

]