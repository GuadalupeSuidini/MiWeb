from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import usuarios
from .forms import datos_usuarios
# Create your views here.


def inicio(request):
    return render(request,"padre.html")
###
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
        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render (request, "padre.html", {"mensaje": f'Usuario {username} creado'})

    else:

        form = UserCreationForm()

    return render(request, "registro.html", {"form": form})



def ingreso_usuario(request):

    if request.method == "POST":

        miformulario = datos_usuarios(request.POST)

        if miformulario.is_valid():

            data = miformulario.cleaned_data

            datos_ingreso = usuarios(nombre=data['nombre'], apellido=data['apellido'], correo=data['correo'], direccion=data['direccion'], nacimiento=data['nacimiento'], celular=data['celular'])
        
            datos_ingreso.save()

            return redirect("Listadedatos")

        return render(request, 'act_datos.html')
    else:

        miformulario = datos_usuarios()


    return render(request, "act_datos.html", {"miformulario": miformulario})


######################################################################################################################