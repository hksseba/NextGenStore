from rest_framework import serializers
from core.models import Usuario
class UsuriaoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Usuario
        fields = ['nombre_usuario','apellido_usuario','apellido_usuario','correo_usuario']