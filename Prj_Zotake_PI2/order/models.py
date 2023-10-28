# Arquivo de modelo de Order 

from django.db import models

class Pedidos (models.Model):
    id_pedidos = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, blank=False, help_text='Insira um nome valido: Nome e Sobrenomes')
    email = models.EmailField(null=True, blank=False, help_text='Insira um e-mail valido: usuario@dominio')
    telefone = models.CharField(max_length=11, null=True, blank=True)
    arquivo = models.ImageField(null=True, blank=True)
    mensagem = models.CharField(null=True, blank=True)
    criacao = models.DateTimeField(null=True, blank=False, auto_now_add=True)

    class Meta:
        ordering =['criacao']
        verbose_name = 'Pedidos recebidos'

    def __str__(self):
        return f'[{self.id_pedidos}]{self.nome}'

    def get_absolute_url(self):
        return reverse('detalhes-pedido', args=[str(self.id_pedidos)])
