from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Selecciones, Noticias, Productos, Chat, Nosotros
from AppCoder.forms import SeleccionesFormulario, NoticiasFormulario, ProductosFormulario, ChatFormulario, NosotrosFormulario

# Create your views here.

def inicio(request):

      return render(request, "AppCoder/home.html")

def selecciones(request):

      return render(request, "AppCoder/selecciones.html")

def noticias(request):

      return render(request, "AppCoder/blogNoticias.html")

def noticia1(request):

      return render(request, "AppCoder/noticia1.html")

def contactos(request):

      return render(request, "AppCoder/contact.html")

def chat(request):

      return render(request, "AppChat/chatFormulario.html")

def nosotros(request):

      return render(request, "AppCoder/nosotros.html")



def seleccionesFormulario(request):

      if request.method == "POST":
            
            miFormularioSelecciones= SeleccionesFormulario(request.POST)
            print(miFormularioSelecciones)

            if miFormularioSelecciones.is_valid:
                  
                  informacion = miFormularioSelecciones.cleaned_data
                  selecciones = Selecciones(nombre=informacion['nombre'], apellido=informacion['apellido'], numerodesocio=informacion['numerodesocio'], email=informacion['email'])
                  selecciones.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormularioSelecciones= SeleccionesFormulario()
      return render(request, "AppCoder/seleccionesFormulario.html",{"miFormulario":miFormularioSelecciones})

def noticiasFormulario(request):

      if request.method == "POST":

            miFormularioNoticias= NoticiasFormulario(request.POST)
            print(miFormularioNoticias)

            if miFormularioNoticias.is_valid:

                  informacion = miFormularioNoticias.cleaned_data
                  noticias = Noticias(nombre=informacion['nombre'], apellido=informacion['apellido'], posicion=informacion['posicion'], numerocamiseta=informacion['numerocamiseta'], email=informacion['email'])
                  noticias.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormularioNoticias= NoticiasFormulario()
      return render (request, "AppCoder/noticiasFormulario.html",{"miFormulario":miFormularioNoticias})

def productosFormulario(request):
      if request.method == "POST":

            miFormularioProductos= ProductosFormulario(request.POST)
            print(miFormularioProductos)

            if miFormularioProductos.is_valid:

                  informacion = miFormularioProductos.cleaned_data
                  productos = Productos(nombre=informacion['nombre'], apellido=informacion['apellido'], contactotelefonico=informacion['contactotelefonico'], email=informacion['email'])
                  productos.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormularioProductos= ProductosFormulario()
      return render (request, "AppCoder/productosFormulario.html",{"miFormulario":miFormularioProductos})

def chatFormulario(request):
      if request.method == "POST":

            miFormularioChat= ChatFormulario(request.POST)
            print(miFormularioChat)

            if miFormularioChat.is_valid:

                  informacion = miFormularioChat.cleaned_data
                  chat = Chat(nombre=informacion['nombre'], apellido=informacion['apellido'], numerofuncionario=informacion['numerofuncionario'], contactotelefonico=informacion['contactotelefonico'], email=informacion['email'])
                  chat.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormularioChat= ChatFormulario()
      return render (request, "AppCoder/chatFormulario.html",{"miFormulario":miFormularioChat})

def productosFormulario(request):
      if request.method == "POST":

            miFormularioProductos= ProductosFormulario(request.POST)
            print(miFormularioProductos)

            if miFormularioProductos.is_valid:

                  informacion = miFormularioProductos.cleaned_data
                  productos = Productos(nombre=informacion['nombre'], apellido=informacion['apellido'], contactotelefonico=informacion['contactotelefonico'], email=informacion['email'])
                  productos.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormularioProductos= ProductosFormulario()
      return render (request, "AppCoder/productosFormulario.html",{"miFormulario":miFormularioProductos})

def nosotrosFormulario(request):
      if request.method == "POST":

            miFormularioNosotros= NosotrosFormulario(request.POST)
            print(miFormularioNosotros)

            if miFormularioNosotros.is_valid:

                  informacion = miFormularioNosotros.cleaned_data
                  nosotros = Nosotros(nombre=informacion['nombre'], apellido=informacion['apellido'], numerofuncionario=informacion['numerofuncionario'], contactotelefonico=informacion['contactotelefonico'], email=informacion['email'])
                  nosotros.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormularioNosotros= NosotrosFormulario()
      return render (request, "AppCoder/nosotrosFormulario.html",{"miFormulario":miFormularioNosotros})

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
      
      
  