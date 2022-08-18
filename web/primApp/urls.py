
from django.urls import path
from .views import act_usuario, inicio, ingreso_usuarios, registro, servicios, lista_usuario

from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', inicio, name = 'inicio'),


############ url ingreso usuarios
    path('login',ingreso_usuarios, name = 'login'),
    path('registar',registro, name = 'registrar'),
    path('usuarios',act_usuario, name = 'usuarios'),
    path('misdatos',lista_usuario, name = 'misdatos'),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name="logout"),
############################################################


     path('servicios', servicios, name = 'servicios'),


]
