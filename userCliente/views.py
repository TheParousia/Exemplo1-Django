from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from app1.models import Cartao

# Create your views here.


def login_user(request):

    if request.method == "POST":
        login_nome = request.POST.get("login")
        senha = request.POST.get("senha")

        user = authenticate(login_nome, senha)

        print(user)

        if user:
            login(request, user)

            redirect('listar_cartao')
        else:
            return render(request, "login.html", {"error": user})

    return render(request, "login.html")


def cadastro_cliente(request):

    if request.method == "POST":
        # Create user and save to the database
        nome_de_usuario = request.POST.get("nome_de_usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        user = User.objects.create_user(nome_de_usuario, email, senha)

        # # Update fields and then save again
        # user.first_name = request.POST.get("primeiro_nome")
        # user.last_name = request.POST.get("ultimo_nome")
        user.save()

        # 1. Criar ou obter o grupo
        grupoClientes, criado = Group.objects.get_or_create(name='cliente')

        # 2. Obter o ContentType do modelo
        content_type = ContentType.objects.get_for_model(Cartao)

        # 3. Obter as permissões definidas no Meta
        permissoes = Permission.objects.filter(
            codename__in=['pode_atualizar', 'pode_criar'],
            content_type=content_type
        )
        # 4. Atribuir as permissões ao grupo
        grupoClientes.permissions.add(*permissoes)

        user.groups.add(grupoClientes)

        return redirect("listar_cartao")

    return render(request, "cadastro_cliente.html")


@login_required
def area_restrica(request):
    return HttpResponse("Bem vindo")
