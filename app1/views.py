import os
from pathlib import Path
from app1 import models
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import permission_required
from django.core.files.storage import FileSystemStorage
from django.conf import settings


# ++
fs = FileSystemStorage()


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

    if request.method == "POST":
        file_name = fs.save('img.jpg', request.FILES['imagem'])
        url = fs.url(file_name)
        print(url)
        cartao = models.Cartao()
        cartao.nome = request.POST.get("nome")
        cartao.remetente = request.POST.get("remetente")
        cartao.mensagem = request.POST.get("mensagem")
        cartao.imagem = url

        cartao.save()

        return redirect("listar_cartao")

    return render(request, "formulario_post.html")


def deletar_cartao(request, id):
    # Obtem os dados do banco de dados de um cartão com o id especifico
    # cartao = models.Cartao.objects.get(id=id)
    cartao = get_object_or_404(models.Cartao, id=id)

    nome_arquivo = os.path.basename(cartao.imagem.url)

    caminho_completo = os.path.join(settings.MEDIA_ROOT, nome_arquivo)

    if os.path.exists(caminho_completo):
        os.remove(caminho_completo)

    cartao.delete()

    return redirect("listar_cartao")


def atualizar_cartao(request, id):
    # Obtem os dados do banco de dados de um cartão com o id especifico
    cartao = models.Cartao.objects.get(id=id)

    context = {
        "cartao": cartao
    }

    if request.method == "POST":
        cartao.nome = request.POST.get("nome")
        cartao.remetente = request.POST.get("remetente")
        cartao.mensagem = request.POST.get("mensagem")

        if 'imagem' in request.FILES:
            print('imagem' in request.POST)
            file_name = fs.save('img.jpg', request.FILES['imagem'])
            url = fs.url(file_name)
            cartao.imagem = url

        cartao.save()

        return redirect("listar_cartao")

    return render(request, "formulario_atualizar.html", context)


def novo_cliente(request):
    template = loader.get_template("novo_cliente.html")
    return HttpResponse(template.render())


def listar_cartao(request):
    print(request.user.id)

    cartoes = models.Cartao.objects.all().values()

    context = {
        "cartoes": cartoes
    }

    return render(request, "listar_cartao.html", context)


def listar_cartaoH(request):
    cartoes = models.Cartao.objects.all().values()
    context = {
        "cartoes": cartoes
    }

    template = loader.get_template("listar_cartao.html")
    return HttpResponse(template.render(context, request))
