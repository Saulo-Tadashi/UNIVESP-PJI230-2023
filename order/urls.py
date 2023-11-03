# Arquivo de mapeamento URL de Order

from django.urls import path, re_path
from order import views

urlpatterns = [
    path('pedido-enviado/', views.enviar_pedidos, name='pedido'),
    path('lista/', views.PedidosListView.as_view(), name = 'pedidos'),
    re_path(r'^lista/(?P<mode>\w+)', views.PedidosListView.as_view(), name = 'pedidos-filtro'),
    re_path(r'^(?P<pk>\d+)$', views.PedidosUpdate.as_view(), name='detalhes-pedido'),
]