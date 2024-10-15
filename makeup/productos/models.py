from django.db import models

# Create your models here.
# models.py

class usuario(models.Model):
        usuario= models.AutoField(primary_key=True)
        password = models.CharField(max_length=6)
        direccion = models.CharField(max_length=50)
        telefono = models.IntegerField(max_length=10)

class Product(models.model):
        product_id =models.Avg
        nombre = models.AutoField
        precio = models.CharField
        descripcion = models.CharField
        stock = models.constraints
        imagen = models.ImageField

# Ejemplo de cómo usar los modelos

if __name__ == "__main__":
    # Crear un usuario
    user = User(user_id=1, name="Juan Perez", email="juan.perez@example.com")
    print(user.get_info())

    # Crear un producto
    product = Product(product_id=101, name="Laptop", price=1200.99)
    print(product.get_info())
