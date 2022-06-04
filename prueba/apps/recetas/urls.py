from django.urls import path, include
from django.contrib.auth.decorators import login_required

from apps.recetas.views import index, recetas_view, recetas_list, recetas_edit, recetas_delete,\
    RecetasList, RecetasCreate, RecetasUpdate, RecetasDelete

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', login_required(RecetasCreate.as_view()), name='recetas_crear'),
    path('listar/', login_required(RecetasList.as_view()), name='recetas_listar'),
    path('editar/<pk>/', login_required(RecetasUpdate.as_view()), name='recetas_editar'),
    path('eliminar/<pk>/', login_required(RecetasDelete.as_view()), name='recetas_eliminar'),
]
