from django.contrib import admin
from django.urls import path, include
from .views import agradecimiento, buscador, carrito
urlpatterns = [
    path('', agradecimiento,name="Recibo"),
    path('Productos', buscador,name="Buscar productos"),
    path('Carrito',carrito, name="carrito")
]