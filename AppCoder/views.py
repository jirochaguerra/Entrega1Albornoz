from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Funcionarios, Hinchas, Jugadores, Dirigentes
from AppCoder.forms import FuncionariosFormulario, HinchasFormulario, JugadoresFormulario, DirigentesFormulario

# Create your views here.

def inicio(request):

      return render(request, "AppCoder/inicio.html")

def hinchas(request):

      return render(request, "AppCoder/hinchas.html")

def jugadores(request):

      return render(request, "AppCoder/jugadores.html")

def dirigentes(request):

      return render(request, "AppCoder/dirigentes.html")

def funcionarios(request):

      return render(request, "AppCoder/funcionarios.html")

def hinchasFormulario(request):

      if request.method == "POST":
            
            miFormularioHinchas= HinchasFormulario(request.POST)
            print(miFormularioHinchas)

            if miFormularioHinchas.is_valid:
                  
                  informacion = miFormularioHinchas.cleaned_data
                  hinchas = Hinchas(nombre=informacion['nombre'], apellido=informacion['apellido'], numerodesocio=informacion['numerodesocio'], email=informacion['email'])
                  hinchas.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormularioHinchas= HinchasFormulario()
      return render(request, "AppCoder/hinchasFormulario.html",{"miFormulario":miFormularioHinchas})

def jugadoresFormulario(request):

      if request.method == "POST":

            miFormularioJugadores= JugadoresFormulario(request.POST)
            print(miFormularioJugadores)

            if miFormularioJugadores.is_valid:

                  informacion = miFormularioJugadores.cleaned_data
                  jugadores = Jugadores(nombre=informacion['nombre'], apellido=informacion['apellido'], posicion=informacion['posicion'], numerocamiseta=informacion['numerocamiseta'], email=informacion['email'])
                  jugadores.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormularioJugadores= JugadoresFormulario()
      return render (request, "AppCoder/jugadoresFormulario.html",{"miFormulario":miFormularioJugadores})

def dirigentesFormulario(request):
      if request.method == "POST":

            miFormularioDirigentes= DirigentesFormulario(request.POST)
            print(miFormularioDirigentes)

            if miFormularioDirigentes.is_valid:

                  informacion = miFormularioDirigentes.cleaned_data
                  dirigentes = Dirigentes(nombre=informacion['nombre'], apellido=informacion['apellido'], contactotelefonico=informacion['contactotelefonico'], email=informacion['email'])
                  dirigentes.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormularioDirigentes= DirigentesFormulario()
      return render (request, "AppCoder/dirigentesFormulario.html",{"miFormulario":miFormularioDirigentes})

def funcionariosFormulario(request):
      if request.method == "POST":

            miFormularioFuncionarios= FuncionariosFormulario(request.POST)
            print(miFormularioFuncionarios)

            if miFormularioFuncionarios.is_valid:

                  informacion = miFormularioFuncionarios.cleaned_data
                  funcionarios = Funcionarios(nombre=informacion['nombre'], apellido=informacion['apellido'], numerofuncionario=informacion['numerofuncionario'], contactotelefonico=informacion['contactotelefonico'], email=informacion['email'])
                  funcionarios.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormularioFuncionarios= FuncionariosFormulario()
      return render (request, "AppCoder/funcionariosFormulario.html",{"miFormulario":miFormularioFuncionarios})

def busquedaNombre(request):

      hincha= []
      if request.method == "POST":
            nombre= request.POST.get('nombre')
            hincha= Hinchas.objects.filter(nombre__icontains=nombre)

      contexto = {
            'my_form': Hinchas(),
            'hinchas': hincha
      }
      return render(request, "AppCoder/busquedaNombre.html", contexto)
      
      
      
      
      # hinchas = []
      # if request.method == "POST":
      #       nombre = request.POST.get('nombre')
      #       hinchas = Hinchas.objects.filter(nombre__icontains=nombre)
      #       return render(request, "AppCoder/busquedaNombre.html", {"hinchas":Hinchas(), "nombre":nombre})
      # else:
      #       respuesta= "No enviaste datos"
      #       return HttpResponse(respuesta)



# def buscar(request):

#       if request.GET["nombre"]:
#             nombre = request.GET['nombre']
#             hinchas= Hinchas.objects.filter(nombre__icontains=nombre)
#             return render(request, "AppCoder/resultadosBusqueda.html", {"hinchas":Hinchas(), "nombre":nombre})
#       else:
#             respuesta= "No enviaste datos"
#             return HttpResponse(respuesta)
#       #respuesta = f"Estoy buscando el nombre: {request.GET['nombre']}"
            



