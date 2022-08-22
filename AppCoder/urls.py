from django.urls import path
from AppCoder import views

urlpatterns = [
   
    path('', views.inicio), #esta era nuestra primer view
    path('funcionarios', views.funcionarios, name="Funcionarios"),
    path('hinchas', views.hinchas, name="Hinchas" ),
    path('jugadores', views.jugadores, name="Jugadores"),
    path('dirigentes', views.dirigentes, name="Dirigentes"),
    path('hinchasFormulario', views.hinchasFormulario, name="HinchasFormulario"),
    path('jugadoresFormulario', views.jugadoresFormulario, name="JugadoresFormulario"),
    path('dirigentesFormulario', views.dirigentesFormulario, name="DirigentesFormulario"),
    path('funcionariosFormulario', views.funcionariosFormulario, name="FuncionariosFormulario"),
    path('busquedaNombre', views.busquedaNombre, name="BusquedaNombre"),
]