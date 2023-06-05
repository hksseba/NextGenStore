from django.contrib import admin
from django.urls import path, include
from rest_api.views import lista_usuarios
urlpatterns = [
    path('lista_usuarios', lista_usuarios,name="lista_usuarios"),
    

]