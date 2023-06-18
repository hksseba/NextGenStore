from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Usuario,Producto
from .serializers import UsuriaoSerializer, UsuarioSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_usuarios(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuriaoSerializer(usuario ,many  = True )
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuriaoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
@api_view(['GET','PUT','DELETE'])   
@permission_classes((IsAuthenticated,))
def detalle_usuarios(request,id):
    try:
        usuario = Usuario.objects.get(id_usuario = id)
    except Usuario.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialiazer = UsuriaoSerializer(usuario)
        return Response(serialiazer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serialiazer = UsuriaoSerializer(usuario, data = data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response(serialiazer.data)
        else:
            return Response(serialiazer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method  == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@csrf_exempt
@api_view(['GET','POST'])   
@permission_classes((IsAuthenticated,))
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
         

@api_view(['GET','PUT','DELETE'])   
@permission_classes((IsAuthenticated,))
def detalle_productos(request,id):
    try:
        producto = Producto.objects.get(id_producto = id)

    except Producto.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialiazer = UsuarioSerializer(producto)
        return Response(serialiazer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serialiazer = UsuarioSerializer(producto, data = data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response(serialiazer.data)
        else:
            return Response(serialiazer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method  == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)