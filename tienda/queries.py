from tienda.models import Cliente, Producto, Pedido
from django.utils import timezone
from datetime import timedelta

# ===============================
# 20 CONSULTAS TABLAS INDIVIDUALES
# ===============================

# CLIENTE
clientes = Cliente.objects.all()
clientes_activos = Cliente.objects.filter(activo=True)
clientes_inactivos = Cliente.objects.filter(activo=False)
cliente_por_correo = Cliente.objects.get(correo="luis@example.com")
clientes_hoy = Cliente.objects.filter(fecha_registro__date=timezone.now().date())
clientes_ordenados = Cliente.objects.order_by("nombre")
total_clientes = Cliente.objects.count()

# PRODUCTO
productos = Producto.objects.all()
productos_caros = Producto.objects.filter(precio__gt=100)
productos_baratos = Producto.objects.filter(precio__lt=50)
producto_laptop = Producto.objects.get(nombre__iexact="GPU externa")
productos_gaming = Producto.objects.filter(descripcion__icontains="Aceleradora")
productos_por_precio = Producto.objects.order_by("precio")
total_productos = Producto.objects.count()

# PEDIDO
pedidos = Pedido.objects.all()
pedidos_pagados = Pedido.objects.filter(estado="PAGADO")
pedidos_hoy = Pedido.objects.filter(fecha__date=timezone.now().date())
pedidos_recientes = Pedido.objects.order_by("-fecha")
total_pedidos = Pedido.objects.count()
pedidos_no_cerrados = Pedido.objects.exclude(estado="CERRADO")

# ===============================
# 10 CONSULTAS A DOS TABLAS
# ===============================

pedidos_juan = Pedido.objects.filter(cliente__nombre="Ana Ruiz")
pedidos_clientes_activos = Pedido.objects.filter(cliente__activo=True)
productos_pedidos_pagados = Producto.objects.filter(pedidos__estado="PAGADO").distinct()
clientes_con_pedidos = Cliente.objects.filter(pedidos__isnull=False).distinct()
clientes_sin_pedidos = Cliente.objects.filter(pedidos__isnull=True)
pedidos_con_laptop = Pedido.objects.filter(productos__nombre__iexact="GPU externa")
productos_de_ana = Producto.objects.filter(pedidos__cliente__nombre="Ana Ruiz").distinct()
pedidos_clientes_hoy = Pedido.objects.filter(cliente__fecha_registro__date=timezone.now().date())
productos_enviados = Producto.objects.filter(pedidos__estado="ENVIADO").distinct()
clientes_pagados = Cliente.objects.filter(pedidos__estado="PAGADO").distinct()

# ===============================
# 5 CONSULTAS A TRES TABLAS
# ===============================

productos_clientes_activos = Producto.objects.filter(
    pedidos__cliente__activo=True
).distinct()

productos_pagados_activos = Producto.objects.filter(
    pedidos__estado="PAGADO",
    pedidos__cliente__activo=True
).distinct()

clientes_compraron_laptop = Cliente.objects.filter(
    pedidos__productos__nombre__iexact="GPU externa"
).distinct()

pedidos_pagados_caros = Pedido.objects.filter(
    estado="PAGADO",
    productos__precio__gt=100
).distinct()

clientes_activos_enviados_baratos = Cliente.objects.filter(
    activo=True,
    pedidos__estado="ENVIADO",
    pedidos__productos__precio__lt=50
).distinct()