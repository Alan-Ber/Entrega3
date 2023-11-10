"""
URL configuration for Entrega3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# URLS generales del proyecto

from Entrega3.views import inicio, posts, perfiles, comentarios, crear_post, crear_perfil, crear_comentario, lista_posts,buscar_perfil

urlpatterns =[ path("admin/", admin.site.urls),
    path("inicio/", inicio, name="inicio"),
    path("posts/", posts, name="entradas"),
    path("perfiles/", perfiles, name="perfiles"),
    path("comentarios/", comentarios),
    path("crear-post/", crear_post, name="crear_post"),
    path("crear-perfil/", crear_perfil, name="crear_perfil"),
    path("crear-comentario/", crear_comentario, name="crear_comentario"),
    path("listado-entradas/", lista_posts, name="lista_posts")
    path("busqueda-perfil/",buscar_perfil,name="buscar_perfil")
]
