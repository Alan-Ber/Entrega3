from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_post = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo}"


class Comentario(models.Model):
    nombre = models.CharField(max_length=256)
    contenido = models.TextField()
    fecha_post = models.DateTimeField(auto_now_add=True)


class PerfilUsuario(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
