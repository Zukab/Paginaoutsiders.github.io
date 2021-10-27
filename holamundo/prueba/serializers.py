from rest_framework import serializers
from .models import *

class categoriasSerializer (serializers.ModelSerializer):
    class Meta:
        model = categorias
        fields = ['id', 'nombre' , 'estado' , 'fecha_creacion']


class AutorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombres','apellidos','correo']

