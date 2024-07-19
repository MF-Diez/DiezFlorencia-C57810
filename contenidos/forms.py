from django import forms
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ConsejosForm(forms.Form):
    nombreRed= forms.CharField(max_length=50, required=True, label="Nombre de la Red Social")
    desarrollo= forms.CharField(max_length=300, required=True, label="Describí tu consejo")
    nombreAutor=forms.CharField(max_length=80, required=True, label="Ingresa tu nombre o @ ")
    
class MusicaForm(forms.Form):
    artista= forms.CharField(max_length=50, required=True, label="Nombre del Artista o Banda")
    titulo=forms.CharField(max_length=80, required=True, label="Nombre de la canción")
    estilo=forms.CharField(max_length=80, required=True, label="Estilo musical")
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=80, required=True, label="Ingrese su Nombre")
    last_name = forms.CharField(max_length=80, required=True, label="Ingrese su Apellido")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirme Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email","first_name", "last_name", "password1", "password2" ]

    