from socket import fromshare
from unittest.util import _MAX_LENGTH
from django import forms

class JugadoresFormulario(forms.Form):
    pais= forms.CharField(max_length=30)
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    nacimiento= forms.DateField()
    posicion = forms.CharField(max_length=30)

class NosotrosFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)  
    contactotelefonico= forms.IntegerField()
    email= forms.EmailField()

class ContactosFormulario(forms.Form):
    email= forms.EmailField()
    nombre= forms.CharField(max_length=30)
    contactotelefonico= forms.IntegerField()
    mensaje = forms.CharField(max_length=1000000)
