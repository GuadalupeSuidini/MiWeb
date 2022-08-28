from multiprocessing import AuthenticationError

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, UserRegisterForm

from .models import mascotas, usuarios
from .forms import datos_mascotas, datos_usuarios

# Create your views here.


def inicio(request):
    
    return render(request,"padre.html")


########################################################################################3

def servicios(request):
    return render(request,"services.html")
#############################################################33
# ingreso y registro de ususarios   
def ingreso_usuarios(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = data["username"]
            passw = data["password"]

            ingreso = authenticate(username=user, password=passw)

            if ingreso:
                login(request, ingreso)

                return render(request,"padre.html", {"mensaje": f"Bienvenido {user}"})

            else:

                return render(request,"erroringreso.html", {"mensaje":"Error, Datos Incorrectos"})
        return render(request,"erroringreso.html", {"mensaje":"Error, Datos Incorrectos"})
    else: 

        form = AuthenticationForm()

        return render(request,"ingreso.html", {'form':form})

def registro(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render (request, "padre.html", {"mensaje": f'Usuario {username} creado'})

    else:

        form = UserRegisterForm()

    return render(request, "registro.html", {"form": form})



#def ing_usuario(request):
    

#    if request.method == "POST":

#        miformulario = datos_usuarios(request.POST)

#        if miformulario.is_valid():

#            data = miformulario.cleaned_data

#            datos_usu = usuarios(nombre=data['nombre'], apellido=data['apellido'], correo=data['correo'], direccion=data['direccion'], nacimiento=data['nacimiento'], pais=data['pais'], departamento=data['departamento'], celular=data['celular'], entidad=data['entidad'])
        
#            datos_usu.save()

 #           return redirect("inicio")

 #       return render(request, 'ingresardatos.html')
 #   else:

  #      miformulario = datos_usuarios()


   # return render(request, "ingresardatos.html", {"miformulario": miformulario})


def ing_usuarios(request):
    data = {
        'form': datos_usuarios()

    }

    if request.method == 'POST':
        formulario = datos_usuarios(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario
            
    return render(request, 'ingresardatos.html', data)        

def lista_usuario (request):

    lista_usu = usuarios.objects.all()

    contexto = {"lista_usu": lista_usu}

    return render(request, "misdatos.html", contexto)

def eliminardatos(request, id):

    if request.method == "POST":
        
        datos = usuarios.objects.get(id=id)

        datos.delete()

        lista_usu = usuarios.objects.all()

        contexto = {"lista_usu": lista_usu}

        return render(request,"padre.html", contexto)


def editarusuario(request, id):

    usuario = usuarios.objects.get(id=id)

    if request.method == 'POST':

        formulario = datos_usuarios(request.POST)
        

        if formulario.is_valid():

            data = formulario.cleaned_data

            usuario.nombre = data['nombre']
            usuario.apellido = data['apellido']
            usuario.correo = data['correo']
            usuario.direccion = data['direccion']
            usuario.nacimiento = data['nacimiento']
            usuario.pais = data['pais']
            usuario.departamento = data['departamento']
            usuario.celular = data['celular']
            usuario.entidad = data['entidad']

            usuario.save()

            return render(request, "misdatos.html")
    else: 

        formulario= datos_usuarios(initial={
        'nombre' :  usuario.nombre, 
        'apellido' : usuario.apellido,
        'correo' : usuario.correo,
        'direccion' : usuario.direccion,
        'nacimiento' : usuario.nacimiento, 
        'pais' : usuario.pais, 
        'departamento' : usuario.departamento, 
        'celular' : usuario.celular, 
        'entidad' : usuario.entidad, 
        })

    return render(request, "act_datos.html", {"formulario":formulario, "id":usuario.id})

######################################################################################################################

#### mascota

def datos_mascota(request):

    if request.method == "POST":

        mascota = datos_mascotas(request.POST, files=request.FILES)

        if mascota.is_valid():

            data = mascota.cleaned_data

            datos_animal = mascotas(nombre=data['nombre'], raza=data['raza'], edad=data['edad'], vacunas=data['vacunas'], descripcion=data['descripcion'], imagen=data['imagen'])
        
            datos_animal.save()

            return redirect("inicio")

        return render(request, 'datos_mascotas.html')
    else:

        mascota = datos_mascotas()


    return render(request, "datos_mascotas.html", {"mascota": mascota})

def lista_mascotas (request):

    lista_mas = mascotas.objects.all()

    contexto = {"lista_mas": lista_mas}

    return render(request, "mismascotas.html", contexto)
    
#def modificar_mascota (request, id):

#    mascota = mascotas.objects.get(id=id)
#    data = {
#        'form': datos_mascotas(instance=mascota)
#    }
#    if request.method == 'POST':
#        formulario = datos_mascotas(data=request.POST, instance=mascota, files=request.FILES)
#        if formulario.is_valid():
#            formulario.save()
#            data['mensaje'] = "modificado "
#            data['form']= formulario
#        return render(request, 'mismascotas.html', data)


def modificar_mascota(request, id):

    usuario = mascotas.objects.get(id=id)

    if request.method == 'POST':

        formulario = datos_mascotas(request.POST)
        

        if formulario.is_valid():

            data = formulario.cleaned_data

            usuario.nombre = data['nombre']
            usuario.raza = data['raza']
            usuario.edad = data['edad']
            usuario.vacunas = data['vacunas']
            usuario.descripcion = data['descripcion']
            usuario.imagen = data['imagen']
         

            usuario.save()

            return render(request, "mismascotas.html")
    else: 

        formulario= datos_mascotas(initial={
        'nombre' :  usuario.nombre, 
        'raza' : usuario.raza,
        'edad' : usuario.edad,
        'vacunas' : usuario.vacunas,
        'descripcion' : usuario.descripcion, 
        'imagen' : usuario.imagen, 
       
        })

    return render(request, "modificarmascota.html", {"formulario":formulario, "id":usuario.id})