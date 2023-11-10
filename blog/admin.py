from django.contrib import admin

from blog.models import PerfilUsuario, Post, Comentario

admin.site.register(PerfilUsuario)
admin.site.register(Post)
admin.site.register(Comentario)
