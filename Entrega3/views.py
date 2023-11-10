from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import *
from django.urls import reverse


def inicio(request):
    contexto = {
        "Entradas": Post.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response


def posts(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='posts.html',
        context=contexto,
    )
    return http_response


def perfiles(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='perfiles.html',
        context=contexto,
    )
    return http_response


def comentarios(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='comentarios.html',
        context=contexto,
    )
    return http_response


# def crear_post(request):
    http_response = render(
        request=request,
        template_name='formulario_entrada.html',
    )
    return http_response


def crear_perfil(request):
    http_response = render(
        request=request,
        template_name='formulario_perfil.html',
    )
    return http_response


def crear_comentario(request):
    http_response = render(
        request=request,
        template_name='formulario_comentario.html',
    )
    return http_response


def crear_post(request):
    if request.method == "POST":
        data = request.POST
        post = Post(titulo=data['nombre'])
        post.save()
        url_exitosa = reverse('lista_posts')
        return redirect(url_exitosa)
    else:  # GET
        return render(
            request=request,
            template_name='formulario_entrada.html',)


def lista_posts(request):
    contexto = {"Entradas": Post.objects.all()

                }
    http_response = render(
        request=request,
        template_name='lista_entradas.html',
        context=contexto,
    )
    return http_response


def buscar_perfil(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        perfiles = PerfilUsuario.objects.filter(
            PerfilUsuario__contains=busqueda)
        contexto = {
            "perfiles": PerfilUsuario,
        }
        http_response = render(
            request=request,
            template_name='lista_perfiles.html',
            context=contexto,
        )
        return http_response
