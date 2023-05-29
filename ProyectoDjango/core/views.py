from django.shortcuts import render, redirect
from .models import Producto,Pedido,Usuario,Rol,Pregunta
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

def ingresarProducto(request):
    vId = request.POST['Id del producto']
    vNombre = request.POST['nombreProducto']
    vDesc = request.POST['Descripcion del producto']
    vPrecio = request.POST['Precio']
    vFoto = request.FILES['ejemplo_archivo_1']
    vStock = request.POST['StockProducto']

    vProducto = Producto.objects.get(codigo = vId)
    Producto.objects.create(nombre_producto = vNombre, desc_producto = vDesc, precio_producto = vPrecio, fotoProducto = vFoto, stock_producto = vStock, id_producto = vProducto)
    
    return redirect('PovAdmin')

def inicioSesion (request):
    lista = Usuario.objects.all()
    contexto = {
        "Usuario": lista
    }
    return render(request,'core/html/InicioSesion.html', contexto) 

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
    vId = request.POST['Id del usuario']
    vRut = request.POST['Rut del usuario']
    vNombre = request.POST['nombre']
    vApellido = request.POST['apellido']
    vTelefono = request.POST['telefono']
    vCorreo = request.POST['email']
    vClave = request.POST['contrasena']
    vRespuesta = request.POST['respuesta']
    vPregunta = request.Post['lang']

    Usuario.objects.create(id_usuario = vId, rut = vRut, nombre_usuario = vNombre, apellido_usuario = vApellido, telefono_usuario = vTelefono, correo_usuario = vCorreo, clave_usuario = vClave, respuesta_usuario = vRespuesta, pregunta = vPregunta)
    
    return redirect('ingresarproducto')
 
def RestablecerContrasena (request):
    vClave = request.POST['contrasena']
    Usuario.objects.create(clave_usuario = vClave)

    return render(request,'core/html/RestablecerContrasena.html')

def Usuario (request):      
    lista = Usuario.objects.all()
    contexto = {
        "productos": lista
    }
    return render(request,'core/html/Usuario.html', contexto)