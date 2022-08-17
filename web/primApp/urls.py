
from django.urls import path
from .views import ingreso_usuario, inicio, ingreso_usuarios, registro

from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', inicio, name = 'inicio'),


############ url ingreso usuarios
    path('login',ingreso_usuarios, name = 'login'),
    path('registar',registro, name = 'registrar'),
    path('usuarios',ingreso_usuario, name = 'usuarios'),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name="logout"),




]
