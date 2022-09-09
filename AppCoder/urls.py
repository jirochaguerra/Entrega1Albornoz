from django.urls import path
from AppCoder import views

urlpatterns = [
   
    path('inicio', views.inicio, name="Inicio"),
    path('hinchasFormulario', views.hinchasFormulario, name="HinchasFormulario"),
    path('jugadoresFormulario', views.jugadoresFormulario, name="JugadoresFormulario"),
    path('dirigentesFormulario', views.dirigentesFormulario, name="DirigentesFormulario"),
    path('funcionariosFormulario', views.funcionariosFormulario, name="FuncionariosFormulario"),
    path('busquedaNombre', views.busquedaNombre, name="BusquedaNombre"),
]