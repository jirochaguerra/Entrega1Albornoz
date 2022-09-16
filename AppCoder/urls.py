from django.urls import path
from AppCoder import views
from AppChat import views3

urlpatterns = [
   
    path('home/', views.inicio, name="home"),
    path('seleccionesFormulario', views.seleccionesFormulario, name="SeleccionesFormulario"),
    path('noticiasFormulario', views.noticiasFormulario, name="NoticiasFormulario"),
    path('productosFormulario', views.productosFormulario, name="ProductosFormulario"),
    path('chatFormulario', views.chatFormulario, name="ChatFormulario"),
    path('nosotrosFormulario', views.nosotrosFormulario, name="NosotrosFormulario"), 
    path('busquedaNombre', views.busquedaNombre, name="BusquedaNombre"),
    path('AppChat', views3.home, name="AppChat"),
    #path('A', views3.home, name='home'),
    path('<str:room>/', views3.room, name='room'),
    path('checkview', views3.checkview, name='checkview'),
    path('send', views3.send, name='send'),
    path('getMessages/<str:room>/', views3.getMessages, name='getMessages'),
]