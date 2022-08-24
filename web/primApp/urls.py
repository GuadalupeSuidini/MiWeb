
from django.urls import path
from .views import act_usuario, datos_mascota, inicio, ingreso_usuarios, registro, servicios, lista_usuario

from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', inicio, name = 'inicio'),


############ url ingreso usuarios
    path('Login',ingreso_usuarios, name = 'login'),
    path('Registar',registro, name = 'registrar'),
    path('Usuarios',act_usuario, name = 'usuarios'),
    path('Misdatos',lista_usuario, name = 'misdatos'),
    path('Logout/',LogoutView.as_view(template_name='logout.html'), name="logout"),
############################################################


     path('Servicios', servicios, name = 'servicios'),

##########################################################3
     path('Mascotas', datos_mascota, name = 'mascotas'),
]
