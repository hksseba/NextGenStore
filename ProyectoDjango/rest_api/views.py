from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Usuario,Producto
from .serializers import UsuriaoSerializer, UsuarioSerializer


@csrf_exempt
@api_view(['GET','POST'])
def lista_usuarios(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuriaoSerializer(usuario ,many  = True )
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuriaoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTPP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTPP_400_BAD_REQUEST )
        
@csrf_exempt
@api_view(['GET','POST'])     
def lista_productos (request):
    if request.method == 'GET':
        producto = Producto.objects.filter(stock_producto = 0 )
        serializer = UsuarioSerializer(producto , many  = True )
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTPP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTPP_400_BAD_REQUEST )
         