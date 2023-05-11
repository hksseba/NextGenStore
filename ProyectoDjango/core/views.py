from django.shortcuts import render

# Create your views here.
def agradecimiento(request):
    return render(request, 'core/html/Agradecimiento.html')

def buscador (request):
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

def Producto2 (request):
    return render(request,'core/html/Producto2.html') 

def Producto3 (request):
    return render(request,'core/html/Producto3.html') 

def Producto4 (request):
    return render(request,'core/html/Producto4.html') 

def Producto5 (request):
    return render(request,'core/html/Producto5.html') 

def Producto6 (request):
    return render(request,'core/html/Producto6.html') 

def Producto7 (request):
    return render(request,'core/html/Producto7.html') 

def Producto8 (request):
    return render(request,'core/html/Producto8.html') 

def Producto9 (request):
    return render(request,'core/html/Producto9.html') 

def Producto10 (request):
    return render(request,'core/html/Producto10.html') 

def Producto11 (request):
    return render(request,'core/html/Producto11.html') 
 
def RegistroUsuario (request):
    return render(request,'core/html/RegistroUsuario.html') 
 
def RestablecerContraseña (request):
    return render(request,'core/html/RestablecerContraseña.html')

def Usuario (request):
    return render(request,'core/html/Usuario.html')    