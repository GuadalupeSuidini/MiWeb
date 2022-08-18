from django.db import models



# Create your models here.
class usuarios(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    direccion = models.CharField(max_length=30)
    nacimiento = models.DateTimeField()
    pais = models.CharField(max_length=20)
    departamento = models.CharField(max_length=20)
    celular = models.IntegerField()
    entidad = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido}"