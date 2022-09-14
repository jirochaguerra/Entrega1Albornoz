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
