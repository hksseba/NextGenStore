from django.contrib import admin
from django.urls import path, include
from .views import agregaradmin,formRestablecerContrasena,RestablecerContrasena,agregarCarrito,modificarUsuarios,modificarUsuario,cerrar_sesion,iniciar_sesion,modificarProducto,modificar,eliminarProducto,agregarusuario,agregar, agradecimiento, productos, carrito, celulares, computadores, consolas, direccion, ingresarProducto,inicioSesion,olvidoClave,PaginaPrincipal,PovAdmin,Producto1,RegistroUsuario,RestablecerContrasena,Usuario1,formDireccion,comprobarOlvidoClave,RegistroAdmin

urlpatterns = [
    path('recibo', agradecimiento,name="recibo"),
    path('productos', productos,name="productos"),
    path('carrito',carrito, name="carrito"),
    path('celulares',celulares, name="celulares"),
    path('computadores',computadores, name="computadores"),
    path('consolas',consolas, name="consolas"),
    path('direccion/<int:id_usuario>/',direccion, name="direccion"),
    path('ingresarproducto', ingresarProducto, name="ingresarProducto"),
    path('iniciosesion',inicioSesion, name="iniciosesion"), 
    path('olvidoClave',olvidoClave, name="olvidoclave"),
    path('',PaginaPrincipal, name="paginaprincipal"),
    path('PovAdmin',PovAdmin, name="PovAdmin"),
    path('producto1/<int:id>/',Producto1, name="producto1"),
    path('registrousuario',RegistroUsuario, name="registrousuario"),
    path('usuario',Usuario1, name="usuario"),
    path('formDireccion', formDireccion, name='formDireccion'),
    path('agregar',agregar, name="agregar"),
    path('eliminarProducto/<int:id>',eliminarProducto,name="eliminarProducto"), 
    path('modificar/<int:id_producto>/',modificar,name="modificar"),
    path('modificarProducto/',modificarProducto,name="modificarProducto"),
    path('agregarusuario',agregarusuario, name="agregarusuario"),
    path('iniciar_sesion',iniciar_sesion, name="iniciar_sesion"),
    path('comprobarOlvidoClave',comprobarOlvidoClave, name="comprobarOlvidoClave"),
    path('RestablecerContrasena/<int:id_usuario>/',RestablecerContrasena, name="RestablecerContrasena"),
    path('formRestablecerContrasena',formRestablecerContrasena, name="formRestablecerContrasena"),
    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),
    path('modificarUsuario',modificarUsuario, name="modificarUsuario"),
    path('modificarUsuarios',modificarUsuarios, name="modificarUsuarios"),
    path('agregarCarrito/<int:id_producto>/',agregarCarrito, name="agregarCarrito"),
    path('RegistroAdmin',RegistroAdmin, name="RegistroAdmin"),
    path('agregaradmin',agregaradmin, name="agregaradmin")






]