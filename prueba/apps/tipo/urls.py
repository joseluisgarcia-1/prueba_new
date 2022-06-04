from django.urls import path
from apps.tipo.views import index_tipo, PedidoList, PedidoCreate, PedidoUpdate, PedidoDelete

urlpatterns = [
    path('',  index_tipo, name='inicio'),
    path('tipo/listar', PedidoList.as_view(), name='tipo_listar'),
    path('tipo/nueva', PedidoCreate.as_view(), name='tipo_crear'),
    path('tipo/editar/<pk>/', PedidoUpdate.as_view(), name='tipo_editar'),
    path('tipo/eliminar/<pk>/', PedidoDelete.as_view(), name='tipo_eliminar'),
]
