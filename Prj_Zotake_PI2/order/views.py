# Arquivo View de Order

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from order.models import Pedidos
from order.forms import PedidosAtualizar as Atualizar



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

class PedidosListView(LoginRequiredMixin, generic.ListView):
    model = Pedidos
    context_object_name = 'lista_pedidos'
    template_name = 'pedidos/lista-pedidos.html'
    paginate_by = 15
    login_url = '/users/login/'
    redirect_field_name = '/order/lista/'

    def get_queryset(self):
        return Pedidos.objects.all()

    def get_context_data(self, **kwargs):        
        context = super(PedidosListView, self).get_context_data(**kwargs)        
        context['outros'] = ''
        return context

class PedidosUpdate(LoginRequiredMixin, UpdateView):
    model = Pedidos
    context_object_name = 'objPedido'
    template_name = 'pedidos/detalhes-do-pedido.html'
    login_url = '/users/login/'
    redirect_field_name = '/order/lista/'
    success_url = reverse_lazy('pedidos')

    form_class = Atualizar
