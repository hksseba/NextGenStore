from django.shortcuts import render, redirect
from .models import *
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
    contexto = {
        "productos": lista
    }
    return render(request,'core/html/Celulares.html', contexto) 

def computadores (request):
    lista = Producto.objects.all()
    contexto = {
        "productos": lista
    }
    return render(request, 'core/html/Computadores.html', contexto)

def consolas (request):
    lista = Producto.objects.all()
    contexto = {
        "productos": lista
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
    
    return redirect('paginaprincipal')



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

    usuario = Usuario.objects.create(rol=vRol, nombre_usuario=vNombre, apellido_usuario=vApellido, telefono_usuario=vTelefono, correo_usuario=vCorreo, clave_usuario=vClave, respuesta_usuario=vRespuesta, pregunta=Preguntaxd)
    
    return redirect('direccion', id_usuario=usuario.id_usuario)


 
def RestablecerContrasena (request):
    vClave = request.POST['contrasena']
    Usuario.objects.create(clave_usuario = vClave)

    return render(request,'core/html/RestablecerContrasena.html')

def Usuario1 (request):      
    lista = Usuario.objects.all()
    contexto = {
        "productos": lista
    }
    return render(request,'core/html/Usuario.html', contexto)

