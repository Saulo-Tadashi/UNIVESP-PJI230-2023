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
    try:
        pedido.nome = request.POST.get('nome')
        pedido.email = request.POST.get('email')
        pedido.telefone = request.POST.get('telefone')
        pedido.mensagem = request.POST.get('mensagem')
        pedido.arquivo = request.FILES.get('exemplo')

        if pedido.nome is None or pedido.email is None:
            raise ValidationError(_('O preenchimento do nome e e-mail e obrigatorio!'))

        pedido.save()

        obj = {
            'pedido' : pedido,       
        }

        return render(request, 'pedidos/sucesso-pedido.html', obj)
    except Exception as e:
        raise e
    

class PedidosListView(LoginRequiredMixin, generic.ListView):
    model = Pedidos
    context_object_name = 'lista_pedidos'
    template_name = 'pedidos/lista-pedidos.html'
    paginate_by = 8
    login_url = '/users/login/'
    redirect_field_name = '/order/lista/'

    def get_queryset(self):
        pedidos = Pedidos.objects.all()
        if self.request.path == reverse('pedidos'):
            pedidos = Pedidos.objects.all().order_by('criacao')
        elif self.kwargs["mode"] == 'orcamento':
            pedidos = Pedidos.objects.filter(envio_orcamento__isnull=False).order_by('envio_orcamento')
        elif self.kwargs["mode"] == 'prazo':
            pedidos = Pedidos.objects.filter(prazo__isnull=False).order_by('prazo')
        elif self.kwargs["mode"] == 'pagamento':
            pedidos = Pedidos.objects.filter(pagamento__isnull=False).order_by('pagamento')
        elif self.kwargs["mode"] == 'despacho':
            pedidos = Pedidos.objects.filter(despacho__isnull=False).order_by('despacho')
        elif self.kwargs["mode"] == 'conclusao':
            pedidos = Pedidos.objects.filter(conclusao__isnull=False).order_by('conclusao')
        return pedidos

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
