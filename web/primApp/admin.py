from django.contrib import admin
from .models import usuarios
# Register your models here.
class usuariosAdmin(admin.ModelAdmin):
    
    list_display = ["nombre", "apellido", "correo", "direccion", "nacimiento","pais", "departamento", "celular", "entidad"]
    search_fields = ["nombre"]


admin.site.register(usuarios, usuariosAdmin)