from dataclasses import field, fields
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import mascotas, usuarios



class UserRegisterForm(UserCreationForm):
   
    password1 = forms.CharField(label='Contraseña',widget= forms.PasswordInput)
    password2 = forms.CharField(label='Contraseña',widget= forms.PasswordInput)
    class meta:
        model = User
        fields = {'username','password1','password2'}
        help_texts = {k:"" for k in fields }

class datos_usuarios(forms.ModelForm):

    class Meta:
        model = usuarios
        fields = '__all__'

        widgets = {
            "nacimiento": forms.SelectDateWidget()
        } 


class datos_mascotas(forms.ModelForm):

    class Meta:
        
        model = mascotas
        fields = '__all__'


   