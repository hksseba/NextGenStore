from django.contrib import admin
from django.urls import path, include
from .views import agradecimiento, buscador, carrito, celulares, computadores, consolas, ingresarProducto,inicioSesion,olvidoClave,PaginaPrincipal,PovAdmin,Producto1,RegistroUsuario,RestablecerContraseña,Usuario

urlpatterns = [
    path('Recibo', agradecimiento,name="Recibo"),
    path('Productos', buscador,name="Productos"),
    path('Carrito',carrito, name="Carrito"),
    path('Celulares',celulares, name="Celulares"),
    path('Computadores',computadores, name="Computadores"),
    path('Consolas',consolas, name="Consolas"),
    path('Ingresar Producto', ingresarProducto, name="IngresarProducto"),
    path('Inicio seion',inicioSesion, name="InicioSesion"), 
    path('Olvido Clave',olvidoClave, name="OlvidoClave"),
    path('Pagina ',PaginaPrincipal, name="PaginaPrincipal"),
    path('',PovAdmin, name="PovAdmin"),
    path('Producto1',Producto1, name="Producto1"),
    path('Registro',RegistroUsuario, name="RegistroUsuario"),
    path('Restablecer Contraseña',RestablecerContraseña, name="RestablecerContraseña"),
    path('Usuario',Usuario, name="Usuario"),
]