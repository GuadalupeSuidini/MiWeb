from django import forms


class datos_usuarios(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    direccion = forms.CharField()
    nacimiento = forms.DateField()
    celular = forms.IntegerField()