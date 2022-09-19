from django.db import models

# Create your models here.

class Selecciones(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    numerodesocio= models.IntegerField()
    email= models.EmailField()

class Noticias(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    posicion= models.CharField(max_length=20)
    numerocamiseta=models.IntegerField()
    email= models.EmailField()

class Productos(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)  
    contactotelefonico= models.IntegerField()
    email= models.EmailField()

class Chat(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)  
    numerofuncionario= models.IntegerField()
    contactotelefonico= models.IntegerField()
    email= models.EmailField()

class Nosotros(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)  
    contactotelefonico= models.IntegerField()
    email= models.EmailField()

class jugadoresSelecciones(models.Model):
    pais = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento = models.DateField()
    posicion = models.CharField(max_length=30)