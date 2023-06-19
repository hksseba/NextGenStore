from django.contrib import admin
from django.urls import path, include
from rest_api.views import lista_usuarios,lista_productos,detalle_usuarios,detalle_productos,crear_productos
from rest_api.viewsLogin import login
urlpatterns = [
    path('lista_usuarios', lista_usuarios,name="lista_usuarios"),
    path('detalle_usuarios/<int:id>', detalle_usuarios,name="detalle_usuarios"),
    path('lista_productos', lista_productos,name="lista_productos"),
    path('detalle_productos/<int:id>', detalle_productos,name="detalle_productos"),
    path('crear_productos', crear_productos,name="crear_productos"),
    path('login', login ,name="login"),

]