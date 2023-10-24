from django.db import models

class Pedidos (models.Model):
    id_pedidos = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)
    telefone = models.CharField(max_length=11)
    arquivo = models.ImageField(blank=True)
    mensagem = models.CharField(blank=False)
    criacao = models.DateTimeField(auto_now_add=True)
