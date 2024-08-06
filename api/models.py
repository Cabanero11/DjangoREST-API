from django.db import models

# Create your models here.
class BlogPost(models.Model):
    # id lo hace automatico
    titulo = models.CharField(max_length=120)
    contenido = models.TextField()
    # Se pone sola la fecha :o
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title