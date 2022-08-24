
from xml.dom.minidom import Document
from django.urls import path
from .views import act_usuario, datos_mascota, eliminardatos, inicio, ingreso_usuarios, lista_mascotas, modificar_mascota, registro, servicios, lista_usuario, editarusuario

from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', inicio, name = 'inicio'),


############ url ingreso usuarios
    path('Login',ingreso_usuarios, name = 'login'),
    path('Registar',registro, name = 'registrar'),
    path('Usuarios',act_usuario, name = 'usuarios'),
    path('Misdatos',lista_usuario, name = 'misdatos'),
    path('Logout/',LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('edita-datos/<int:id>',editarusuario, name = 'ediusuarios'),
    path('elimina-datos/<int:id>',eliminardatos, name = 'eliminardatos'),
############################################################


     path('Servicios', servicios, name = 'servicios'),

##########################################################3
     path('Mascotas', datos_mascota, name = 'mascotas'),
     path('Mismascotas',lista_mascotas, name = 'mismascotas'),
     path('Modificarmascotas/<int:id>',modificar_mascota, name = 'modmascotas'),

]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)