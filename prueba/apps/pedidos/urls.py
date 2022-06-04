from django.urls import path, include
from django.contrib.auth.decorators import login_required

from apps.pedidos.views import index, pedidos_view, pedidos_list, pedidos_edit, pedidos_delete,\
    PedidosList, PedidosCreate, PedidosUpdate, PedidosDelete

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', login_required(PedidosCreate.as_view()), name='pedidos_crear'),
    path('listar/', login_required(PedidosList.as_view()), name='pedidos_listar'),
    path('editar/<pk>/', login_required(PedidosUpdate.as_view()), name='pedidos_editar'),
    path('eliminar/<pk>/', login_required(PedidosDelete.as_view()), name='pedidos_eliminar'),
]
