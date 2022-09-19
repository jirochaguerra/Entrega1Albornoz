from django.urls import path
from AppCoder import views
from AppChat import views3

urlpatterns = [
   
    path('home/', views.inicio, name="Inicio"),
    path('selecciones/', views.selecciones, name="Selecciones"),
    path('noticias/', views.noticias, name="Noticias"),
    path('noticia1/', views.noticia1, name="Noticia1"),
    path('contactos/', views.contactos, name="Contactos"),
    path('chat/', views.chat, name="Chat"),
    path('nosotros/', views.nosotros, name="Nosotros"), 
    path('busquedaNombre', views.busquedaNombre, name="BusquedaNombre"),
    path('chat/', views3.home, name="AppChat"),
    path('AppChat', views3.home, name="AppChat"),
    #path('A', views3.home, name='home'),
    path('<str:room>/', views3.room, name='room'),
    path('checkview', views3.checkview, name='checkview'),
    path('send', views3.send, name='send'),
    path('getMessages/<str:room>/', views3.getMessages, name='getMessages'),
]