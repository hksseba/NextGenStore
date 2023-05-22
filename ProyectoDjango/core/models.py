from django.db import models

# Create your models here.
class Rol (models.Model):
    id_rol = models.AutoField(primary_key = True, verbose_name='Id del rol')
    nombre_rol = models.CharField(max_length=20, verbose_name='Nombre del rol', null = True, blank = False)

class Pregunta (models.Model):
    id_pregunta  = models.AutoField(primary_key = True, verbose_name='Id de la pregunta')
    nombre_pregunta = models.CharField(max_length=20, verbose_name='Nombre de la pregunta', null = True, blank = False)

class Region (models.Model):
    id_region = models.AutoField(primary_key = True, verbose_name='Id de la region')
    nombre_region = models.CharField(max_length=20, verbose_name='Nombre de la region', null = True, blank = False)

class Categoria (models.Model):
    id_categoria  = models.AutoField(primary_key = True, verbose_name='Id de la categoria')
    nombre_categoria = models.CharField(max_length=20, verbose_name='Nombre de la categoria', null = True, blank = False)

class Comuna (models.Model):
    id_comuna  = models.AutoField(primary_key = True, verbose_name='Id de la comuna')
    nombre_comuna = models.CharField(max_length=20, verbose_name='Nombre de la comuna', null = True, blank = False)
    costo_dia = models.IntegerField(max_length=20, verbose_name='costo por dia', null = True, blank = False)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)

class Producto (models.Model):
    id_producto  = models.AutoField(primary_key = True, verbose_name='Id del producto')
    nombre_producto = models.CharField(max_length=20, verbose_name='Nombre del producto', null = True, blank = False)
    desc_producto = models.CharField(max_length=100, verbose_name='Descripcion del producto', null = True, blank = False)
    precio_producto = models.IntegerField(max_length=20, verbose_name='Precio del producto', null = True, blank = False)
    foto_producto = models.ImageField(max_length=20, verbose_name='Imagen del producto', null = True, blank = False)
    stock_producto = models.IntegerField(max_length=20, verbose_name='Stock del producto', null = True, blank = False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

class Usuario (models.Model):


class Pedido (models.Model):


class Direccion (models.Model):
    id_direccion  = models.AutoField(primary_key = True, verbose_name='Id de la direccion')
    nombre_direccion = models.CharField(max_length=20, verbose_name='Nombre de la direccion', null = True, blank = False)
    num_direccion = models.IntegerField(max_length=10, verbose_name='Numero de la direccion', null = True, blank = False)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Detalle (models.Model):
    id_detalle  = models.AutoField(primary_key = True, verbose_name='Id de la direccion')
    cantidad = models.IntegerField(max_length=20, verbose_name='Cantidad de productos', null = True, blank = False)
    subtotal = models.IntegerField(max_length=10, verbose_name='Subtotal', null = True, blank = False)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)


   