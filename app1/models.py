from django.db import models

# Create your models here.


class Cartao(models.Model):
    nome = models.CharField(max_length=30)
    remetente = models.CharField(max_length=30)
    mensagem = models.TextField(max_length=255)
    imagem = models.ImageField()
