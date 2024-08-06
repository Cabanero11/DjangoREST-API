from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostCrearLista(generics.ListCreateAPIView):
    # Obtener todos los objetos BlogPost
    # (queryset, serializer_class) obligatorio nombre
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # Tras crear el view, se enlaca con su URL

    # Crear otra funcion, diferentes al DELETE base de DJANGO
    # Spawnea un boton en http://127.0.0.1:9000/blogposts/ de DELETE
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Para acceder a diferentes BlogPost mediante su id (su primary key)
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # Añadimos para obtener el primary-key -> pk : id
    lookup_field = 'pk'


# Custom APIView 

class BlogPostLista(APIView):
    # get, put, post, etc
    def get(self, request, format=None):
        # Obtener el titulo, sino string vacio ''
        titulo = request.query_params.get('titulo', '')

        # Filtrar si esta el titulo
        if titulo:
            blog_post = BlogPost.objects.filter(title__icontains=titulo)
        else:
            blog_post = BlogPost.objects.all()

        # Devolver una respuesta con los datos serializados y con 200 OK
        serializer = BlogPostSerializer(blog_post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

