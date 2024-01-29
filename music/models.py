from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.db.models.fields.files import FieldFile
from django.contrib.auth.models import User

class musico(models.Model):
     usuario = models.CharField(max_length=30, primary_key=True)
     nombre = models.CharField(max_length=30)
     sexo = models.CharField(max_length=30)
     edad = models.IntegerField()
     region = models.CharField(max_length=30)
     comuna = models.CharField(max_length=30)
     disponibilidad = models.CharField(max_length=30)
     carrera = models.CharField(max_length=30)
     banda = models.CharField(max_length=30) 
     instrumento1 = models.CharField(max_length=30)
     instrumento2 = models.CharField(max_length=30)
     instrumento3 = models.CharField(max_length=30)
     estilo1 = models.CharField(max_length=30)
     estilo2 = models.CharField(max_length=30)
     estilo3 = models.CharField(max_length=30)
     artista1 = models.CharField(max_length=30)
     artista2 = models.CharField(max_length=30)
     artista3 = models.CharField(max_length=30)
     imagen = models.ImageField(upload_to='media/', null=True)

     def __str__(self):
         return self.usuario

class estilo(models.Model):
	usuario = models.CharField(max_length=30, primary_key=True)
	instrumento1 = models.CharField(max_length=30)
	instrumento2 = models.CharField(max_length=30)
	instrumento3 = models.CharField(max_length=30)
	estilo1 = models.CharField(max_length=30)
	estilo2 = models.CharField(max_length=30)
	estilo3 = models.CharField(max_length=30)
	artista1 = models.CharField(max_length=30)
	artista2 = models.CharField(max_length=30)
	artista3 = models.CharField(max_length=30)

	def __str__(self):
		return self.usuario
	
class multimedia(models.Model):
    usuario = models.CharField(max_length=30, primary_key=True)
    imagen1 = models.ImageField(upload_to='media/', null=True)
    imagen2 = models.ImageField(upload_to='media/', null=True)
    imagen3 = models.ImageField(upload_to='media/', null=True)
    imagen4 = models.ImageField(upload_to='media/', null=True)
    imagen5 = models.ImageField(upload_to='media/', null=True)
    video1 = models.FileField(upload_to='media/', null=True)
    video2 = models.FileField(upload_to='media/', null=True)
    video3 = models.FileField(upload_to='media/', null=True)
    video4 = models.FileField(upload_to='media/', null=True)
    video5 = models.FileField(upload_to='media/', null=True)
    audio1 = models.FileField(upload_to='media/', null=True)
    audio2 = models.FileField(upload_to='media/', null=True)
    audio3 = models.FileField(upload_to='media/', null=True)
    audio4 = models.FileField(upload_to='media/', null=True)
    audio5 = models.FileField(upload_to='media/', null=True)

    def __str__(self):
        return self.usuario
    
class datos(models.Model):
	usuario = models.CharField(max_length=30, primary_key=True)
	otros_datos = models.CharField(max_length=300)

	def __str__(self):
         return self.usuario

class contacto(models.Model):
	usuario = models.CharField(max_length=30)
	contacto = models.CharField(max_length=30)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
         return f"{self.usuario} - {self.contacto}"

class mensaje(models.Model):
    usuario = models.CharField(max_length=30)
    para = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=300)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.para}"

class anuncio(models.Model):
    usuario = models.CharField(max_length=30)
    anuncio = models.CharField(max_length=300)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return self.usuario


class mensajeadmin(models.Model):
    usuario = models.CharField(max_length=30)
    correo = models.EmailField(max_length=50)
    mensaje = models.CharField(max_length=300)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return self.usuario




