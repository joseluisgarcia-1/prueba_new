from django.urls import path
from apps.tipo.views import index_tipo, RecetaList, RecetaCreate, RecetaUpdate, RecetaDelete

urlpatterns = [
    path('',  index_tipo, name='inicio'),
    path('tipo/listar', RecetaList.as_view(), name='tipo_listar'),
    path('tipo/nueva', RecetaCreate.as_view(), name='tipo_crear'),
    path('tipo/editar/<pk>/', RecetaUpdate.as_view(), name='tipo_editar'),
    path('tipo/eliminar/<pk>/', RecetaDelete.as_view(), name='tipo_eliminar'),
]
