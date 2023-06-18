from rest_framework import serializers
from core.models import Usuario,Producto
class UsuriaoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Usuario
        fields = ['id_usuario','nombre_usuario','apellido_usuario','telefono_usuario','correo_usuario','clave_usuario','respuesta_usuario', 'pregunta' ,'rol']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta :
        model = Producto
        fields = ['id_producto','nombre_producto','stock_producto']