from django.contrib import admin
from django.urls import path, include
from .views import agradecimiento, productos, carrito, celulares, computadores, consolas, direccion, ingresarProducto,inicioSesion,olvidoClave,PaginaPrincipal,PovAdmin,Producto1,RegistroUsuario,RestablecerContrasena,Usuario

urlpatterns = [
    path('recibo', agradecimiento,name="recibo"),
    path('productos', productos,name="productos"),
    path('carrito',carrito, name="carrito"),
    path('celulares',celulares, name="celulares"),
    path('computadores',computadores, name="computadores"),
    path('consolas',consolas, name="consolas"),
    path('direccion',direccion, name="direccion"),
    path('ingresarproducto', ingresarProducto, name="ingresarproducto"),
    path('iniciosesion',inicioSesion, name="iniciosesion"), 
    path('olvidoclave',olvidoClave, name="olvidoclave"),
    path('',PaginaPrincipal, name="paginaprincipal"),
    path('PovAdmin',PovAdmin, name="PovAdmin"),
    path('producto1',Producto1, name="producto1"),
    path('registrousuario',RegistroUsuario, name="registrousuario"),
    path('restablecercontra',RestablecerContrasena, name="restablecercontra"),
    path('usuario',Usuario, name="usuario"),
]