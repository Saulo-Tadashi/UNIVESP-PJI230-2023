from django.shortcuts import render
from django.conf import settings
from order.models import Pedidos

def enviar_pedidos (request):
    pedido = Pedidos()
    pedido.nome = request.POST.get('nome')
    pedido.email = request.POST.get('email')
    pedido.telefone = request.POST.get('telefone')
    pedido.mensagem = request.POST.get('mensagem')
    pedido.arquivo = request.FILES.get('exemplo')
    pedido.save()

    obj = {
        'pedido' : pedido,       
    }

    return render(request, 'pedidos/sucesso-pedido.html', obj)
