from socket import fromshare
from unittest.util import _MAX_LENGTH
from django import forms

class SeleccionesFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    numerodesocio= forms.IntegerField()
    email= forms.EmailField()

class NoticiasFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    posicion= forms.CharField(max_length=20)
    numerocamiseta=forms.IntegerField()
    email= forms.EmailField()

class ProductosFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    contactotelefonico= forms.IntegerField()
    email= forms.EmailField()

class ChatFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    numerofuncionario= forms.IntegerField()
    contactotelefonico= forms.IntegerField()
    email= forms.EmailField()

class NosotrosFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)  
    contactotelefonico= forms.IntegerField()
    email= forms.EmailField()
