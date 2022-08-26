from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget= forms.PasswordInput)
    password2 = forms.CharField(label='Contraseña',widget= forms.PasswordInput)
    class meta:
        model = User
        fields = {'username','email','password1','password2'}
        help_texts = {k:"" for k in fields }

class datos_usuarios(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    direccion = forms.CharField()
    nacimiento = forms.DateField()
    pais= forms.CharField()
    departamento= forms.CharField()
    celular = forms.IntegerField()
    entidad = forms.CharField()


class datos_mascotas(forms.Form):

    nombre = forms.CharField()
    raza = forms.CharField()
    edad = forms.IntegerField()
    vacunas = forms.CharField()
    descripcion = forms.CharField()
    imagen = forms.ImageField()

   