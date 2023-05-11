from django.contrib import admin
from django.urls import path, include
from .views import agradecimiento, buscador, carrito, celulares, computadores, consolas, ingresarProducto,inicioSesion,olvidoClave,PaginaPrincipal,PovAdmin,Producto1,Producto2,Producto3,Producto4,Producto5,Producto6,Producto7,Producto8,Producto9,Producto10,Producto11,RegistroUsuario,RestablecerContraseña,Usuario

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
    path('Pagina Principal',PaginaPrincipal, name="PaginaPrincipal"),
    path('Administrador',PovAdmin, name="PovAdmin"),
    path('Producto1',Producto1, name="Producto1"),
    path('Producto1',Producto2, name="Producto2"),
    path('Producto1',Producto3, name="Producto3"),
    path('Producto1',Producto4, name="Producto4"),
    path('Producto1',Producto5, name="Producto5"),
    path('Producto1',Producto6, name="Producto6"),
    path('Producto1',Producto7, name="Producto7"),
    path('Producto1',Producto8, name="Producto8"),
    path('Producto1',Producto9, name="Producto9"),
    path('Producto1',Producto10, name="Producto10"),
    path('Producto1',Producto11, name="Producto11"),
    path('',RegistroUsuario, name="RegsitroUsuario"),
    path('Restablecer Contraseña',RestablecerContraseña, name="RestablecerContraseña"),
    path('Usuario',Usuario, name="Usuario"),
]