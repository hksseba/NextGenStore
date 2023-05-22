from django.db import models

# Create your models here.
class Rol (models.Model):
    id_rol = models.AutoField(primary_key = True, verbose_name='Id del rol')
    nombre_rol = models.ChardField(max_length=20, verbose_name='Nombre del rol', null = True, blank = False)

class Pregunta (models.Model):
    id_pregunta  = models.AutoField(primary_key = True, verbose_name='Id de la pregunta')
    nombre_pregunta = models.ChardField(max_length=20, verbose_name='Nombre de la pregunta', null = True, blank = False)
   