from django.db import models

# Create your models here.
class Rol (models.Model):
    id_rol = models.AutoField(primary_key = True, verbose_name='Id del rol')
    nombre_rol = models.CharField(max_length=20, verbose_name='Nombre del rol', null = True, blank = False)

    def __str__(self) -> str:
        return self.nombre_rol

class Pregunta (models.Model):
    id_pregunta  = models.AutoField(primary_key = True, verbose_name='Id de la pregunta')
    nombre_pregunta = models.CharField(max_length=50
    , verbose_name='Nombre de la pregunta', null = True, blank = False)

    def __str__(self) -> str:
        return self.nombre_pregunta

class Region (models.Model):
    id_region = models.AutoField(primary_key = True, verbose_name='Id de la region')
    nombre_region = models.CharField(max_length=20, verbose_name='Nombre de la region', null = True, blank = False)

    def __str__(self) -> str:
        return self.nombre_region

class Categoria (models.Model):
    id_categoria  = models.AutoField(primary_key = True, verbose_name='Id de la categoria')
    nombre_categoria = models.CharField(max_length=20, verbose_name='Nombre de la categoria', null = True, blank = False)

    def __str__(self) -> str:
        return self.nombre_categoria

class Comuna (models.Model):
    id_comuna  = models.AutoField(primary_key = True, verbose_name='Id de la comuna')
    nombre_comuna = models.CharField(max_length=20, verbose_name='Nombre de la comuna', null = True, blank = False)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre_comuna

class Producto (models.Model):
    id_producto  = models.AutoField(primary_key = True, verbose_name='Id del producto')
    nombre_producto = models.CharField(max_length=20, verbose_name='Nombre del producto', null = True, blank = False)
    desc_producto = models.CharField(max_length=100, verbose_name='Descripcion del producto', null = True, blank = False)
    precio_producto = models.IntegerField( verbose_name='Precio del producto', null = True, blank = False)
    foto_producto = models.ImageField( verbose_name='Imagen del producto', null = True, blank = False)
    stock_producto = models.IntegerField(verbose_name='Stock del producto', null = True, blank = False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre_producto

class Usuario (models.Model):
    id_usuario = models.AutoField(primary_key = True, verbose_name='Id del usuario')
    nombre_usuario = models.CharField(max_length=25, verbose_name='Nombre del usuario')
    apellido_usuario = models.CharField(max_length=25, verbose_name='Apellido del usuario')
    telefono_usuario = models.CharField(max_length=9, verbose_name='Telefono del usuario')
    correo_usuario = models.CharField(max_length=40, verbose_name='Correo del usuario')
    clave_usuario = models.CharField(max_length=15, verbose_name='Contraseña del usuario')
    respuesta_usuario = models.CharField(max_length=40, verbose_name='Respuesta secreta del usuario')
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre_usuario

class Pedido (models.Model):
    id_pedido = models.AutoField(primary_key = True, verbose_name='Id del pedido')   
    total_pedido = models.IntegerField( verbose_name='Total del pedido')
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.estado_pedido

class Direccion (models.Model):
    id_direccion  = models.AutoField(primary_key = True, verbose_name='Id de la direccion')
    nombre_direccion = models.CharField(max_length=20, verbose_name='Nombre de la direccion', null = True, blank = False)
    num_direccion = models.CharField(max_length= 4, verbose_name='Numero de la direccion', null = True, blank = False)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre_direccion

class Detalle (models.Model):
    id_detalle  = models.AutoField(primary_key = True, verbose_name='Id de la direccion')
    cantidad = models.IntegerField( verbose_name='Cantidad de productos', null = True, blank = False)
    subtotal = models.IntegerField( verbose_name='Subtotal', null = True, blank = False)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)

   