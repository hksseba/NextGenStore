from django.shortcuts import render

# Create your views here.
def agradecimiento(request):
    return render(request, 'core/html/Agradecimiento.html')

def productos (request):
    return render(request,'core/html/Buscador.html')

def carrito (request):
    return render(request,'core/html/Carrito.html')  

def celulares (request):
    return render(request,'core/html/Celulares.html') 

def computadores (request):
    return render(request, 'core/html/Computadores.html')

def consolas (request):
    return render(request, 'core/html/Consolas.html')

def ingresarProducto(request):
    return render(request,'core/html/IngresarProducto.html')

def inicioSesion (request):
    return render(request,'core/html/InicioSesion.html')

def olvidoClave (request):
    return render(request,'core/html/olvidoClave.html')

def PaginaPrincipal (request):
    return render(request,'core/html/PaginaPrincipal.html')
      
def PovAdmin (request):
    return render(request,'core/html/PovAdmin.html') 
 
def Producto1 (request):
    return render(request,'core/html/Producto1.html') 

def RegistroUsuario (request):
    return render(request,'core/html/RegistroUsuario.html') 
 
def RestablecerContrasena (request):
    return render(request,'core/html/RestablecerContrasena.html')

def Usuario (request):
    return render(request,'core/html/Usuario.html')    