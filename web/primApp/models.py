from django.db import models

# Create your models here.
class usuarios(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    direccion = models.CharField(max_length=30)
    nacimiento = models.DateField()
    celular = models.IntegerField()
    