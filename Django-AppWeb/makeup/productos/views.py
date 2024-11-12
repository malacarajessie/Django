
"""from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Usuario
from .forms import ProductoForm, UsuarioForm


#VISTA PARA PONER TODOS LOS PRODUCTOS EN UNA LISTA
def LISTA_PRODUCTOS (request):
    productos = Producto.objects.all()
    return render(request, 'templates/lista_productos.html', {'productos': productos})



#VISTA QUE CREA UN PRODUCTO
def CREAR  (request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'templates/crear_producto.html', {'form': form})




#ACTUALIZAR UN PRODUCTO QUE YA EXISTE
def ACTUALIZAR (request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'templates/editar_producto.html', {'form': form})



#ELIMINA UN PRODUCTO
def ELIMINAR (request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'templates/eliminar_producto.html', {'producto': producto})


###### Vistas para Usuario


#VER TODOS LOS USUARIOS
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'templates/lista_usuarios.html', {'usuarios': usuarios})



#CREA UNA VISTA PARA UN USUARIO NUEVO
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'templates/crear_usuario.html', {'form': form})




#ACTUALIZA UN USUARIO YA EXISTENTE
def actualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'templates/editar_usuario.html', {'form': form})



#ELIMINAR USUARUIO YA EXISTENTE
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.user.delete()
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'templates/eliminar_usuario.html', {'usuario': usuario})
    """
from django.shortcuts import render
def rimel(request):
    return render(request,'productos/rimel.html')

def inicio(request):
    return render(request,'productos/index.html')