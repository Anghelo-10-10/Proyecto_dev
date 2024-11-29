from django.shortcuts import render, redirect
from ..proyecto_reciclaje.models import Producto, PuntoReciclaje, RegistroReciclaje
from ..proyecto_reciclaje.forms import ProductoForm, RegistroReciclajeForm

# Página principal
def inicio(request):
    """Vista para la página principal"""
    return render(request, 'index.html')  # Cambiamos a index.html para usar el contenido nuevo

# Productos
def lista_productos(request):
    """Vista para mostrar todos los productos registrados"""
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def registrar_producto(request):
    """Vista para registrar un nuevo producto"""
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/registrar_producto.html', {'form': form})

# Puntos de reciclaje
def lista_puntos_reciclaje(request):
    """Vista para mostrar todos los puntos de reciclaje"""
    puntos = PuntoReciclaje.objects.all()
    return render(request, 'reciclaje/lista_puntos_reciclaje.html', {'puntos': puntos})

def registrar_reciclaje(request):
    """Vista para registrar un reciclaje"""
    if request.method == 'POST':
        form = RegistroReciclajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_puntos_reciclaje')
    else:
        form = RegistroReciclajeForm()
    return render(request, 'reciclaje/registrar_reciclaje.html', {'form': form})
