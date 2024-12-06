from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models.py

class usuario(models.Model):
        User= models.OneToOneField(User, on_delete=models.CASCADE)
        password = models.CharField(max_length=6)
        direccion = models.CharField(max_length=255, null=True, blank=True)
        telefono = models.CharField(max_length=255, null=True, blank=True)
def __str__(self):
        return self.user.username

class Product(models.Model):
        nombre = models.CharField(max_length=100) 
        precio = models.DecimalField(max_digits=10, decimal_places=2)
        descripcion = models.TextField()  
        stock = models.IntegerField()  
        fecha_agregado = models.DateTimeField(auto_now_add=True)
def __str__(self):

        return self.nombre

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()





