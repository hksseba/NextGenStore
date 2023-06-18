from rest_framework import serializers
from core.models import Usuario,Direccion,Producto
class UsuriaoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Usuario
        fields = ['nombre_usuario','apellido_usuario','apellido_usuario','correo_usuario']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta :
        model = Producto
        fields = ['id_producto','nombre_producto','stock_producto']