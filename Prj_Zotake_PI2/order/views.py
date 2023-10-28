# Arquivo View de Order

from django.shortcuts import render
from django.conf import settings
from django.views import generic
from django.shortcuts import get_object_or_404
from order.models import Pedidos
from django.contrib.auth.mixins import LoginRequiredMixin

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

class PedidosDetailView(LoginRequiredMixin, generic.DetailView):
    model = Pedidos
    context_object_name = 'objPedido'
    template_name = 'pedidos/detalhes-do-pedido.html'
    login_url = '/users/login/'
    redirect_field_name = '/order/lista/'

    def get(self, request, *args, **kwargs):
        pedido = get_object_or_404(Pedidos, pk=kwargs['pk'])
        context = {'pedido': pedido}
        return render(request, 'pedidos/detalhes-do-pedido.html', context)
