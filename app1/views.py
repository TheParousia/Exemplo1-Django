from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def pagina1(request):
    return HttpResponse("Olá Mundo")


def pagina2(request):
    return HttpResponse("Bem vindo à página do [fulano]")


def cartao(request):
    template = loader.get_template("cartao.html")

    contexto = {
        "nome": request.GET.get("nome"),
        "mensagem": request.GET.get("mensagem"),
        "remetente": request.GET.get("remetente"),
    }

    return HttpResponse(template.render(contexto, request))

def formulario(request):
    template = loader.get_template("formulario.html")
    return HttpResponse(template.render())


def cartao_post(request):
    template = loader.get_template("cartao_post.html")

    contexto = {
        "nome": request.POST.get("nome"),
        "mensagem": request.POST.get("mensagem"),
        "remetente": request.POST.get("remetente"),
    }

    return HttpResponse(template.render(contexto, request))

def formulario_post(request):
    template = loader.get_template("formulario_post.html")
    return HttpResponse(template.render(request=request))

def novo_cliente(request):
    template = loader.get_template("novo_cliente.html")
    return HttpResponse(template.render())

def listar_cartao(request):
    return render(request, "listar_cartao.html")
