from django.shortcuts import render, get_object_or_404
from .models import Producto, Pedido, Cliente


def home(request):
    return render(request, "tienda/home.html", {})
"""
vista de inicio
(Solo muestra una pantilla basica sin datos, los archivos de html se llaman vistas y toca crearlos dentro de una carpeta nueva)
"""

"""Vista para listar los productos"""

def lista_productos(request):
    productos = Producto.objects.all().order_by("nombre")
    return render(request, "tienda/lista_productos.html", {"productos": productos})

"""
Vista de detalle producto
"""
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "tienda/detalle_producto.html", {"producto": producto})
