from django.db import models

# Create your models here.


class Cartao(models.Model):
    nome = models.CharField(max_length=30)
    remetente = models.CharField(max_length=30)
    mensagem = models.TextField(max_length=255)
    imagem = models.ImageField(default='')
    permissions = (
        ("pode_deletar", "Permissão para deletar um cartão"),
        ("pode_atualizar", "Permissão para atualizar um cartão"),
        ("pode_criar", "Permissão para criar um cartão"),
    )
