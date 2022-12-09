from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserLoginForm (forms.Form):
    
    username= forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password= forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserRegister (UserCreationForm):
    
    username= forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1= forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2= forms.CharField(label='Password verification', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class Meta():
    model=User
    fields=['username','email','password2']