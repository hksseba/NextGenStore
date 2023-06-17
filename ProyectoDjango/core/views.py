from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.


def agradecimiento(request):    
    lista = Pedido.objects.all()
    contexto = {
        "pedidos": lista
    }
    return render(request, 'core/html/Agradecimiento.html', contexto)

def productos (request):
    lista = Producto.objects.all()
    contexto = {
        "productos": lista
    }
    return render(request,'core/html/Buscador.html', contexto)

def carrito(request):
    usuario = Usuario.objects.get(correo_usuario=request.user.username)
    try:
        pedido = Pedido.objects.filter(usuario=usuario).latest('id_pedido')
        detalles_pedido = Detalle.objects.filter(pedido=pedido)
        precio_total = sum(detalle.subtotal for detalle in detalles_pedido)
        precio_final = sum(detalle.subtotal for detalle in detalles_pedido) +10000
    except Pedido.DoesNotExist:
        detalles_pedido = []

    contexto = {
        'detalles': detalles_pedido,
        'precio_total': precio_total,
        'precio_final':precio_final
    }
    return render(request, 'core/html/Carrito.html', contexto)


def agregarCarrito (request, id_producto):
    producto = Producto.objects.get (id_producto = id_producto )
    usuario = Usuario.objects.get(correo_usuario = request.user.username)
    pedido, created = Pedido.objects.get_or_create( usuario = usuario)
    Detalle.objects.create(pedido=pedido, producto=producto, cantidad=1, subtotal=producto.precio_producto)
    return redirect('carrito' ) 

def aumentarPedido(request, id_detalle):
    detalle = Detalle.objects.get(id_detalle=id_detalle)
    detalle.cantidad += 1
    detalle.subtotal = detalle.cantidad * detalle.producto.precio_producto
    detalle.save()

    # Redirigir a la vista del carrito nuevamente
    return redirect('carrito')

def disminuirPedido(request, id_detalle):
    detalle = Detalle.objects.get(id_detalle=id_detalle)
    detalle.cantidad -= 1

    if detalle.cantidad <= 0:
        detalle.delete()
        return redirect('carrito')
    else:
        detalle.subtotal = detalle.cantidad * detalle.producto.precio_producto
        detalle.save()

def eliminarPedido(request, id_detalle):
    detalle = Detalle.objects.get(id_detalle=id_detalle)
    detalle.delete()
    return redirect('carrito')

def pagarPedido(request):
      usuario = Usuario.objects.get(correo_usuario=request.user.username)   
      pedido = Pedido.objects.create( usuario = usuario)
    # Redirigir al carrito nuevamente
      return redirect('carrito')

def celulares (request):
    celular = Categoria.objects.get(id_categoria = 1)
    lista = Producto.objects.all().filter(categoria = celular)
    listaCategoria = Categoria.objects.all()
    contexto = {
        "productos": lista,
        "categorias": listaCategoria
    }   
    return render(request,'core/html/Celulares.html', contexto)

def computadores (request):
    computador = Categoria.objects.get(id_categoria = 2)
    lista = Producto.objects.all().filter(categoria = computador)
    listaCategoria = Categoria.objects.all()
    contexto = {
        "productos": lista,
        "categorias": listaCategoria
    }
    return render(request, 'core/html/Computadores.html', contexto)

def consolas (request):
    consola = Categoria.objects.get(id_categoria = 3)
    lista = Producto.objects.all().filter(categoria = consola)
    listaCategoria = Categoria.objects.all()
    contexto = {
        "productos": lista,
        "categorias": listaCategoria
    }
    return render(request, 'core/html/Consolas.html', contexto)

def direccion(request, id_usuario):
    listaComunas = Comuna.objects.all()
    listaRegiones = Region.objects.all()
    contexto = {
        "comunas": listaComunas,
        "regiones": listaRegiones,
        "id_usuario": id_usuario
    }
    return render(request, 'core/html/direccion.html', contexto)


def formDireccion(request):
    
    vComuna = request.POST['comuna']
    vDireccion = request.POST['direccion']
    vNumero = request.POST['numdireccion']
    vRegistroComuna = Comuna.objects.get(id_comuna = vComuna)
  
 
    usuario1 = Usuario.objects.get(id_usuario=request.POST['id_usuario'])
    
    Direccion.objects.create(usuario=usuario1,comuna =vRegistroComuna, nombre_direccion=vDireccion, num_direccion=vNumero)
    
    return redirect('iniciosesion')
   



def ingresarProducto(request):
    listaCategorias = Categoria.objects.all()
    contexto = {
        "categorias": listaCategorias
    }
    return render(request, 'core/html/IngresarProducto.html', contexto)

def agregar (request):
    vNombre = request.POST['nombreProducto']
    vDesc = request.POST['descProducto']
    vPrecio = request.POST['precioProducto']
    vFoto = request.FILES['fotoProducto']
    vStock = request.POST['stockProducto']
    vCategoria = request.POST['categoriaProducto']

    vRegistroCategoria = Categoria.objects.get(id_categoria= vCategoria)
    Producto.objects.create(nombre_producto = vNombre, desc_producto = vDesc, precio_producto = vPrecio, foto_producto = vFoto, stock_producto = vStock, categoria = vRegistroCategoria)
    
    return redirect('ingresarProducto')

def modificar(request, id_producto):
    categorias = Categoria.objects.all()
    productos = Producto.objects.get(id_producto = id_producto)
    contexto = {
        "categorias": categorias,
        "productos": productos
    }
    return render(request,'core/html/ModificarProducto.html',contexto)

def modificarProducto(request):
    vIdproducto = request.POST['id_producto']
    vNombre = request.POST['nombreProducto']
    vDesc = request.POST['descProducto']
    vPrecio = request.POST['precioProducto']
    vStock = request.POST['stockProducto']
    vCategoria = request.POST['categoriaProducto']

    producto = Producto.objects.get(id_producto = vIdproducto)
    producto.nombre_producto = vNombre
    producto.desc_producto = vDesc
    producto.precio_producto = vPrecio
    producto.stock_producto = vStock
    
    categoriaProducto = Categoria.objects.get(id_categoria = vCategoria)
    producto.categoria = categoriaProducto

    producto.save()
    return redirect('PovAdmin')

def eliminarProducto(request,id):
    Productos = Producto.objects.get(id_producto = id)
    Productos.delete()
    return redirect('PovAdmin')

def inicioSesion (request):
    lista = Usuario.objects.all()
    contexto = {
       "Usuario": lista
    }
    return render(request,'core/html/InicioSesion.html',contexto) 

	

def olvidoClave (request):
    lista = Usuario.objects.all()
    listap = Pregunta.objects.all()
    contexto = {
        "usuario": lista,
        "preguntas": listap
    }
    return render(request,'core/html/olvidoClave.html', contexto)

def comprobarOlvidoClave(request):
    vCorreo = request.POST['email']
    vRespuesta = request.POST['respuesta']
    vPregunta = request.POST['pregunta']

    Preguntaxd = Pregunta.objects.get(id_pregunta=vPregunta)
    PreguntaN = Pregunta.objects.all()
    usuario = Usuario.objects.get(correo_usuario = vCorreo )
    if vCorreo == usuario.correo_usuario and   Preguntaxd == usuario.pregunta and vRespuesta == usuario.respuesta_usuario:
        return redirect('RestablecerContrasena', id_usuario = usuario.id_usuario)
    else:
        return redirect('olvidoclave')


def PaginaPrincipal(request):
    lista = Producto.objects.all()
    contexto = {
        "productos": lista,
        "user": request.user
    }
    return render(request, 'core/html/PaginaPrincipal.html', contexto)


def PovAdmin (request):
    lista = Producto.objects.all()
    contexto = {
        "productos": lista
    }
    
    return render(request,'core/html/PovAdmin.html', contexto) 
 
def Producto1 (request, id):
    producto = Producto.objects.get(id_producto=id)   
    contexto = {
        "p": producto
    }
    return render(request,'core/html/Producto1.html', contexto) 

def RegistroAdmin (request):
    lista = Pregunta.objects.all()
    contexto = {
        "preguntas": lista
    }
    return render(request,'core/html/RegistroAdmin.html',contexto)

def agregaradmin(request):
    vNombre = request.POST['nombre']
    vApellido = request.POST['apellido']
    vTelefono = request.POST['telefono']
    vCorreo = request.POST['email']
    vClave = request.POST['contrasena']
    vRespuesta = request.POST['respuesta']
    vPregunta = request.POST['pregunta']
    
    if vCorreo.endswith('@NextGenStore.cl'):

        vRol = Rol.objects.get(id_rol = 2)
    else:
        messages.warning(request, 'El correo no corresponde a un administrador')
        return redirect('RegistroAdmin')
        
    
    Preguntaxd = Pregunta.objects.get(id_pregunta=vPregunta)
    PreguntaN = Pregunta.objects.all()
    if Usuario.objects.filter(correo_usuario=vCorreo).exists():
            # El correo electrónico ya está en uso, realiza una acción apropiada (por ejemplo, mostrar un mensaje de error)
             return render(request, 'core/html/RegistroUsuario.html', { 'nombre': vNombre, 'apellido': vApellido, 'telefono': vTelefono,  'respuesta': vRespuesta, 'pregunta': PreguntaN})
  
    usuario = Usuario.objects.create(rol=vRol, nombre_usuario=vNombre, apellido_usuario=vApellido, telefono_usuario=vTelefono, correo_usuario=vCorreo, clave_usuario=vClave, respuesta_usuario=vRespuesta, pregunta=Preguntaxd)
    user = User.objects.create_user(username = vCorreo, first_name =vNombre ,email = vCorreo, last_name = vApellido, password =vClave )

    return redirect('direccion', id_usuario=usuario.id_usuario)


def RegistroUsuario (request):
    listaxd = Pregunta.objects.all()
    contexto = {
        "preguntas": listaxd
    }
    return render(request,'core/html/RegistroUsuario.html',contexto)
    

def agregarusuario(request):
    vNombre = request.POST['nombre']
    vApellido = request.POST['apellido']
    vTelefono = request.POST['telefono']
    vCorreo = request.POST['email']
    vClave = request.POST['contrasena']
    vRespuesta = request.POST['respuesta']
    vPregunta = request.POST['pregunta']

    if vCorreo.endswith('@NextGenStore.cl'):
        vRol = Rol.objects.get(id_rol = 2)
    else:
        vRol = Rol.objects.get(id_rol=1)
    
    Preguntaxd = Pregunta.objects.get(id_pregunta=vPregunta)
    PreguntaN = Pregunta.objects.all()
    if Usuario.objects.filter(correo_usuario=vCorreo).exists():
            # El correo electrónico ya está en uso, realiza una acción apropiada (por ejemplo, mostrar un mensaje de error)
             return render(request, 'core/html/RegistroUsuario.html', { 'nombre': vNombre, 'apellido': vApellido, 'telefono': vTelefono,  'respuesta': vRespuesta, 'pregunta': PreguntaN})
  
    usuario = Usuario.objects.create(rol=vRol, nombre_usuario=vNombre, apellido_usuario=vApellido, telefono_usuario=vTelefono, correo_usuario=vCorreo, clave_usuario=vClave, respuesta_usuario=vRespuesta, pregunta=Preguntaxd)
    user = User.objects.create_user(username = vCorreo, first_name =vNombre ,email = vCorreo, last_name = vApellido, password =vClave )

    return redirect('direccion', id_usuario=usuario.id_usuario)

def iniciar_sesion(request):
	correo1 = request.POST['email']
	contra1 = request.POST['contra']
	try:
		user1 = User.objects.get( username = correo1)
	except User.DoesNotExist:
		messages.error(request,'El correo la contraseña son incorrectos')
		return redirect('iniciosesion')

	pass_valida = check_password(contra1, user1.password)
	if not pass_valida:
		messages.error(request,'El correo o la contraseña son incorrectos')
		return redirect('iniciosesion')
	usuario2 = Usuario.objects.get(correo_usuario = correo1, clave_usuario = contra1)
	user = authenticate(username=correo1, password=contra1)
	if user is not None:
		login(request, user)
		if(usuario2.rol.id_rol == 2):
			return redirect ('PovAdmin')
		else:
			return redirect('usuario')
	else: 
            return redirect('iniciosesion') 
            
def RestablecerContrasena(request, id_usuario):
    contexto = {
        "id_usuario": id_usuario
    }
    return render(request, 'core/html/RestablecerContrasena.html', contexto)
             
 
def formRestablecerContrasena (request):
    vClave = request.POST['contrasena']
    vClave2 = request.POST['rcontrasena']
    id = request.POST['id_usuario']

    usuario = Usuario.objects.get(id_usuario = id)
    user = User.objects.get(username = usuario.correo_usuario)
    if vClave == vClave2:
        usuario.clave_usuario = vClave
        user.set_password(vClave)
        usuario.save()
        user.save()
    return redirect ('iniciosesion')

@login_required
def Usuario1(request):    
    
    usuario = Usuario.objects.get(correo_usuario = request.user.username)
    direcciones = Direccion.objects.get(usuario = usuario)
    return render(request, 'core/html/Usuario.html', {'usuario': usuario, 'direcciones': direcciones})

def modificarUsuario(request):
    listaComunas = Comuna.objects.all()
    usuario = Usuario.objects.get(correo_usuario = request.user.username)
    direccion = Direccion.objects.get(usuario = usuario)
    contexto = {
        "comunas": listaComunas,
        "datos": usuario,
        "direccion": direccion
    }
    return render(request,'core/html/ModificarUsuario.html',contexto)

def modificarUsuarios(request):
    vNombre = request.POST['nombreM']
    vApellido = request.POST['apellido']
    vTelefono = request.POST['telefono']
    vComuna = request.POST['comuna']
    vDireccion = request.POST['direccion']
    vNumero = request.POST['numdireccion']
    vRegistroComuna = Comuna.objects.get(id_comuna = vComuna)

    usuario = Usuario.objects.get(correo_usuario = request.user.username)
    direccion = Direccion.objects.get(usuario = usuario)
    direccion.comuna = vRegistroComuna
    direccion.nombre_direccion = vDireccion
    direccion.num_direccion =vNumero
    usuario.nombre_usuario = vNombre
    usuario.apellido_usuario = vApellido
    usuario.telefono_usuario = vTelefono
    usuario.nombre_usuario = vNombre
    usuario.nombre_usuario = vNombre
    usuario.save()
    direccion.save()
    return redirect('usuario')

    
def cerrar_sesion(request):
    logout(request)
    return redirect('iniciosesion')
    
