from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404

# Create your views here.

@login_required
def agradecimiento(request):    
    lista = Pedido.objects.all()
    contexto = {
        "pedidos": lista
    }
    return render(request, 'core/html/Agradecimiento.html', contexto)

def productos (request):
    lista = Producto.objects.filter(stock_producto__gt = 0)
    contexto = {
        "productos": lista
    }
    return render(request,'core/html/Buscador.html', contexto)

@login_required
def carrito(request):
    
    usuario = Usuario.objects.get(correo_usuario=request.user.username)
    try:
        pedido = Pedido.objects.filter(usuario=usuario).latest('id_pedido')
        detalles_pedido = Detalle.objects.filter(pedido=pedido)
    except Pedido.DoesNotExist:
        detalles_pedido = []

    precio_total = sum(detalle.subtotal for detalle in detalles_pedido)
    precio_final = precio_total + 10000
    contexto = {
        'detalles': detalles_pedido,
        'precio_total': precio_total,
        'precio_final': precio_final
    }

    if request.method == 'POST' and detalles_pedido:
        if pedido:
        # Marcar el pedido actual como pagado
            pedido.estado_pedido = True
            pedido.save()

        # Descontar el stock de los productos en los detalles del pedido
        for detalle in detalles_pedido:
            producto = Producto.objects.get(id_producto=detalle.producto_id)
            producto.stock_producto -= detalle.cantidad
            producto.save()

        # Crear un nuevo pedido para el usuario
        nuevo_pedido = Pedido.objects.create(usuario=usuario, estado_pedido=0)

        # Actualizar el pedido actual en el contexto con el nuevo pedido
        pedido = nuevo_pedido
        detalles_pedido = Detalle.objects.filter(pedido=pedido)
        contexto['detalles'] = detalles_pedido
    return render(request, 'core/html/Carrito.html', contexto)
  

def agregarCarrito (request, id_producto):
    producto = Producto.objects.get (id_producto = id_producto )
    usuario = Usuario.objects.get(correo_usuario = request.user.username)
    pedido, created = Pedido.objects.get_or_create( usuario = usuario , estado_pedido = 0)
    Detalle.objects.create(pedido=pedido, producto=producto, cantidad=1, subtotal=producto.precio_producto)
    return redirect('carrito' ) 

def aumentarPedido(request, id_detalle):
    detalle = Detalle.objects.get(id_detalle=id_detalle)
    producto = Producto.objects.get(id_producto = detalle.producto_id)
    if detalle.cantidad <= producto.stock_producto -1 :
         detalle.cantidad += 1
         detalle.subtotal = detalle.cantidad * detalle.producto.precio_producto
         detalle.save()  
    else: 
         detalle.cantidad = producto.stock_producto 
    
    return redirect('carrito')
    # Redirigir a la vista del carrito nuevamente
    

def disminuirPedido(request, id_detalle):
    detalle = Detalle.objects.get(id_detalle=id_detalle)
    detalle.cantidad -= 1

    if detalle.cantidad == 0:
        detalle.delete()
        return redirect('carrito')
    else:
        detalle.subtotal = detalle.cantidad * detalle.producto.precio_producto
        detalle.save()
        return redirect('carrito')
        

def eliminarPedido(request, id_detalle):
    detalle = Detalle.objects.get(id_detalle=id_detalle)
    detalle.delete()
    return redirect('carrito')

def celulares (request):
    celular = Categoria.objects.get(id_categoria = 1)
    lista = Producto.objects.all().filter(categoria = celular, stock_producto__gt = 0)
    listaCategoria = Categoria.objects.all()
    contexto = {
        "productos": lista,
        "categorias": listaCategoria
    }   
    return render(request,'core/html/Celulares.html', contexto)

def computadores (request):
    computador = Categoria.objects.get(id_categoria = 2)
    lista = Producto.objects.all().filter(categoria = computador, stock_producto__gt = 0)
    listaCategoria = Categoria.objects.all()
    contexto = {
        "productos": lista,
        "categorias": listaCategoria
    }
    return render(request, 'core/html/Computadores.html', contexto)

def consolas (request):
    consola = Categoria.objects.get(id_categoria = 3)
    lista = Producto.objects.all().filter(categoria = consola, stock_producto__gt = 0)
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

@login_required(login_url='iniciosesion')
def DireccionAdmin(request, id_usuario):
    usuario = Usuario.objects.get(correo_usuario = request.user.username)
    if usuario.rol_id == 1:
        listaComunas = Comuna.objects.all()
        listaRegiones = Region.objects.all()
        contexto = {
            "comunas": listaComunas,
            "regiones": listaRegiones,
            "id_usuario": id_usuario
        }
        return render(request, 'core/html/DireccionAdmin.html', contexto)
    else:
         return redirect('paginaprincipal')

def formDireccionAdmin(request):
    
    vComuna = request.POST['comuna']
    vDireccion = request.POST['direccion']
    vNumero = request.POST['numdireccion']
    vRegistroComuna = Comuna.objects.get(id_comuna = vComuna)
  
    usuario1 = Usuario.objects.get(id_usuario=request.POST['id_usuario'])
    
    Direccion.objects.create(usuario=usuario1,comuna =vRegistroComuna, nombre_direccion=vDireccion, num_direccion=vNumero)
    
    return redirect('PovAdmin')

@login_required(login_url='iniciosesion')   
def ingresarProducto(request):
    usuario = Usuario.objects.get(correo_usuario = request.user.username)
    if usuario.rol_id == 1:
        listaCategorias = Categoria.objects.all()
        contexto = {
        "categorias": listaCategorias
        }
        return render(request, 'core/html/IngresarProducto.html', contexto)
    
    else:
         return redirect('paginaprincipal')

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

@login_required(login_url='iniciosesion')
def modificar(request, id_producto):
    usuario = Usuario.objects.get(correo_usuario = request.user.username)
    if usuario.rol_id == 1:
        categorias = Categoria.objects.all()
        productos = Producto.objects.get(id_producto = id_producto)
        contexto = {
            "categorias": categorias,
            "productos": productos
        }
        return render(request,'core/html/ModificarProducto.html',contexto)
    else:
         return redirect('paginaprincipal')

@login_required
def modificarProducto(request):
    usuario = Usuario.objects.get(correo_usuario=request.user.username)
    if usuario.rol_id == 1:
        vIdproducto = request.POST['id_producto']
        vNombre = request.POST['nombreProducto']
        vDesc = request.POST['descProducto']
        vPrecio = request.POST['precioProducto']
        vStock = request.POST['stockProducto']
        vCategoria = request.POST['categoriaProducto']

        producto = Producto.objects.get(id_producto=vIdproducto)
        producto.nombre_producto = vNombre
        producto.desc_producto = vDesc
        producto.precio_producto = vPrecio
        producto.stock_producto = vStock

        # Verificar si se ha proporcionado una nueva foto
        if 'fotoProducto' in request.FILES:
            vFoto = request.FILES['fotoProducto']
            producto.foto_producto = vFoto

        categoriaProducto = Categoria.objects.get(id_categoria=vCategoria)
        producto.categoria = categoriaProducto

        producto.save()
        return redirect('PovAdmin')
    else:
        return redirect('paginaprincipal')

  
  

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
    if vCorreo != usuario.correo_usuario and Preguntaxd != usuario.pregunta and vRespuesta != usuario.respuesta_usuario:
        return redirect('olvidoclave')
    else:
        return redirect('RestablecerContrasena', id_usuario = usuario.id_usuario)
       


def PaginaPrincipal(request):
    lista = Producto.objects.filter(stock_producto__gt = 0 )
    contexto = {
        "productos": lista,
        "user": request.user
    }
    return render(request, 'core/html/PaginaPrincipal.html', contexto)

@login_required(login_url='iniciosesion')  
def PovAdmin(request):
    usuario = Usuario.objects.get(correo_usuario = request.user.username)
    if usuario.rol_id == 1:  # Verificar si el rol es de administrador
        lista = Producto.objects.all()  # Volver a obtener la lista actualizada de productos
        contexto = {
            "productos": lista
        }

        return render(request, 'core/html/PovAdmin.html', contexto)
    else:
        # Redirigir a una página de acceso denegado u otra acción apropiada para usuarios no administradores
        return redirect('paginaprincipal')


def Producto1 (request, id):
    producto = Producto.objects.get(id_producto=id)   
    contexto = {
        "p": producto
    }
    return render(request,'core/html/Producto1.html', contexto) 

@login_required(login_url='iniciosesion')  
def RegistroAdmin (request):
     usuario = Usuario.objects.get(correo_usuario = request.user.username)
     if usuario.rol_id == 1:
        lista = Pregunta.objects.all()
        contexto = {
        "preguntas": lista
        }
        return render(request,'core/html/RegistroAdmin.html',contexto)
     else:
        return redirect('paginaprincipal')

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

        return redirect('DireccionAdmin', id_usuario=usuario.id_usuario)
     
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
        vRol = Rol.objects.get(id_rol = 1)
    else:
        vRol = Rol.objects.get(id_rol=2)
    
    Preguntaxd = Pregunta.objects.get(id_pregunta=vPregunta)
    PreguntaN = Pregunta.objects.all()
    if Usuario.objects.filter(correo_usuario=vCorreo).exists():     
            messages.warning(request, 'El correo ya está en uso')           
            # El correo electrónico ya está en uso, realiza una acción apropiada (por ejemplo, mostrar un mensaje de error)
            return redirect('registrousuario')
  
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
		if(usuario2.rol.id_rol == 1):
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

@login_required(login_url='iniciosesion')  
def Usuario1(request):    
    usuario = Usuario.objects.get(correo_usuario = request.user.username)
    direcciones = Direccion.objects.get(usuario = usuario)
    pedidos = Pedido.objects.filter(estado_pedido=True, usuario=usuario)
    detalles = Detalle.objects.filter(pedido__in=pedidos)


    return render(request, 'core/html/Usuario.html', {'usuario': usuario, 'direcciones': direcciones, 'detalles': detalles })

@login_required(login_url='iniciosesion')  
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
    
