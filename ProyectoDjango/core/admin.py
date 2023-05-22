from django.contrib import admin
from .models import Rol, Pregunta, Region, Categoria, Comuna, Producto, Usuario, Pedido, Direccion, Detalle
# Register your models here.
admin.site.register(Rol)
admin.site.register(Pregunta)
admin.site.register(Region)
admin.site.register(Categoria)
admin.site.register(Comuna)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(Direccion)
admin.site.register(Detalle)
