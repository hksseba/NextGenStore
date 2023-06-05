from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

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

def carrito (request):
    lista = Producto.objects.all()
    contexto = {
        "productos": lista
    }
    return render(request,'core/html/Carrito.html',contexto)  

def celulares (request):
    lista = Producto.objects.all()
    listaCategoria = Categoria.objects.all()
    contexto = {
        "productos": lista,
        "categorias": listaCategoria
    }
    return render(request,'core/html/Celulares.html', contexto) 

def computadores (request):
    lista = Producto.objects.all()
    listaCategoria = Categoria.objects.all()
    contexto = {
        "productos": lista,
        "categorias": listaCategoria
    }
    return render(request, 'core/html/Computadores.html', contexto)

def consolas (request):
    lista = Producto.objects.all()
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
    contexto = {
        "Usuario": lista
    }
    return render(request,'core/html/olvidoClave.html', contexto)

def PaginaPrincipal (request):
    lista = Producto.objects.all()
    contexto = {
        "productos": lista
    }
    return render(request,'core/html/PaginaPrincipal.html', contexto)
      
def PovAdmin (request):
    lista = Producto.objects.all()
    contexto = {
        "productos": lista
    }
    return render(request,'core/html/PovAdmin.html', contexto) 
 
def Producto1 (request):
    lista = Producto.objects.all()
    contexto = {
        "productos": lista
    }
    return render(request,'core/html/Producto1.html', contexto) 

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
		user1 = User.objects.get(username = correo1)
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
			contexto = {"usuario":usuario2}
			
			return render(request,'core/html/PaginaPrincipal.html', contexto)
	else: 
            return redirect( 'iniciosesion') 
            
             
 
def RestablecerContrasena (request):
    vClave = request.POST['contrasena']
    Usuario.objects.create(clave_usuario = vClave)

    return render(request,'core/html/RestablecerContrasena.html')

def Usuario1 (request):      
    lista = Usuario.objects.all()
    contexto = {
        "productos": lista
    }
    
    if rol_usuario == 1:
        # Renderizar una plantilla específica para el rol 1
        return render(request, 'plantilla_rol1.html', contexto)
    elif rol_usuario == 2:
        # Renderizar una plantilla específica para el rol 2 (admin)
        return render(request, 'plantilla_admin.html', contexto)
    

    

