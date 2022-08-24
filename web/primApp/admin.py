from django.contrib import admin
from .models import mascotas, usuarios
# Register your models here.
class usuariosAdmin(admin.ModelAdmin):
    
    list_display = ["nombre", "apellido", "correo", "direccion", "nacimiento","pais", "departamento", "celular", "entidad"]
    search_fields = ["nombre"]

class mascotasAdmin(admin.ModelAdmin):
    
    list_display = ["nombre", "raza", "edad", "vacunas", "descripcion", "imagen"]
    search_fields = ["nombre"]


admin.site.register(usuarios, usuariosAdmin)
admin.site.register(mascotas, mascotasAdmin)