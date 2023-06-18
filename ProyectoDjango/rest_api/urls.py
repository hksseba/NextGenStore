from django.contrib import admin
from django.urls import path, include
from rest_api.views import lista_usuarios,lista_productos
urlpatterns = [
    path('lista_usuarios', lista_usuarios,name="lista_usuarios"),
    path('lista_productos', lista_productos,name="lista_productos"),
    

]