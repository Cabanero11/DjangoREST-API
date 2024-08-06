# Un serializer, toma una instancia
# de un objeto (clase creada)
# y lo convierte en algo para devolver

from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    # Meta clase (eh? es consciente de si misma)
    class Meta:
        # model y fields obligatorios
        model = BlogPost
        fields = ['id', 'titulo', 'contenido', 'fecha_publicacion']
