from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.recetas.forms import PedidosForm
from apps.recetas.models import Pedidos
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    return render(request, 'recetas/index.html')


def recetas_view(request):
    if request.method =='POST':
        form = PedidosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('recetas_listar')
    else:
        form = PedidosForm()
    return render(request, 'recetas/recetas_form.html', {'form':form})

def recetas_list(request):
    recetas = Pedidos.objects.all().order_by('id')
    contexto = {'recetas':recetas}
    return render(request, 'recetas/recetas_list.html', contexto)

def recetas_edit(request, id_recetas):
    recetas = Pedidos.objects.get(id=id_recetas)
    if request.method == 'GET':
        form = PedidosForm(instance=recetas)
    else:
        form = PedidosForm(request.POST, instance=recetas)
        if form.is_valid():
            form.save()
        return redirect('recetas_listar')
    return render(request, 'recetas/recetas_form.html', {'form':form})

def recetas_delete(request, id_recetas):
    recetas = Pedidos.objects.get(id=id_recetas)
    if request.method =='POST':
        recetas.delete()
        return redirect('recetas_listar')
    return render(request, 'recetas/recetas_delete.html', {'recetas':recetas})

class RecetasList(ListView):
    model = Pedidos
    template_name = 'recetas/recetas_list.html'
    paginate_by = 2

class RecetasCreate(CreateView):
    model = Pedidos
    form_class = PedidosForm
    template_name = 'recetas/recetas_form.html'
    success_url = reverse_lazy('recetas_listar')

class RecetasUpdate(UpdateView):
    model = Pedidos
    form_class = PedidosForm
    template_name = 'recetas/recetas_form.html'
    success_url = reverse_lazy('recetas_listar')

class RecetasDelete(DeleteView):
    model = Pedidos
    template_name = 'recetas/recetas_delete.html'
    success_url = reverse_lazy('recetas_listar')

