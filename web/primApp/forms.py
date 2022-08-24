from django import forms



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

   