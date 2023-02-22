from django.db import models

# Create your models here.

# Create your models here.
class Servicios(models.Model):
    servicio =models.CharField(max_length=40)
    descripcion =models.TextField(max_length=100)
    precio= models.FloatField()
    imagen=models.ImageField(upload_to = 'imagenes', null=True)
class Empleados(models.Model):
    dni = models.IntegerField()
    nombre =models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email=models.EmailField()
    categoria=models.CharField(max_length=40)
    imagen=models.ImageField(upload_to = 'imagenes', null=True)
class Entregables(models.Model):
    nombreservicio =models.CharField(max_length=40)
    cliente=models.CharField(max_length=40)
    fecha_de_entrega= models.DateField()
    entregado=models.BooleanField()
    imagen=models.ImageField(upload_to = 'imagenes', null=True)
class Cliente(models.Model):
    dni = models.IntegerField()
    nombre =models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email=models.EmailField()    
class Opiniones(models.Model):
    autor=models.CharField(max_length=40, default="")
    opinion=models.TextField(max_length=240)
    calificacion=models.IntegerField()