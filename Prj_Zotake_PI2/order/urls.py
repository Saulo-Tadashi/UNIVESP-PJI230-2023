from django.urls import path
from order import views


urlpatterns = [
    # path('produtos/', views.home, name='produtos'),
    path('pedido-enviado/', views.enviar_pedidos, name='pedido'),
    # path('sobre/', views.home, name='sobre'),
    # path('contato/', views.home, name='contato'),
]