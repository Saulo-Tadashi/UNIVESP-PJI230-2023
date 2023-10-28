# Arquivo configuração de acesso administrativo do app Order

from django.contrib import admin
from order.models import Pedidos

@admin.register(Pedidos)
class PedidosAdmin (admin.ModelAdmin):
    list_display = ('id_pedidos', 'nome', 'email', 'criacao')
    list_filter = ('criacao', 'nome')