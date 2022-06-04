from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.pedidos.forms import PedidosForm
from apps.pedidos.models import Pedidos
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    return render(request, 'pedidos/index.html')


def pedidos_view(request):
    if request.method =='POST':
        form = PedidosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pedidos_listar')
    else:
        form = PedidosForm()
    return render(request, 'pedidos/pedidos_form.html', {'form':form})

def pedidos_list(request):
    pedidos = Pedidos.objects.all().order_by('id')
    contexto = {'pedidos':pedidos}
    return render(request, 'pedidos/pedidos_list.html', contexto)

def pedidos_edit(request, id_pedidos):
    pedidos = Pedidos.objects.get(id=id_pedidos)
    if request.method == 'GET':
        form = PedidosForm(instance=pedidos)
    else:
        form = PedidosForm(request.POST, instance=pedidos)
        if form.is_valid():
            form.save()
        return redirect('pedidos_listar')
    return render(request, 'pedidos/pedidos_form.html', {'form':form})

def pedidos_delete(request, id_pedidos):
    pedidos = Pedidos.objects.get(id=id_pedidos)
    if request.method =='POST':
        pedidos.delete()
        return redirect('pedidos_listar')
    return render(request, 'pedidos/pedidos_delete.html', {'pedidos':pedidos})

class PedidosList(ListView):
    model = Pedidos
    template_name = 'pedidos/pedidos_list.html'
    paginate_by = 2

class PedidosCreate(CreateView):
    model = Pedidos
    form_class = PedidosForm
    template_name = 'pedidos/pedidos_form.html'
    success_url = reverse_lazy('pedidos_listar')

class PedidosUpdate(UpdateView):
    model = Pedidos
    form_class = PedidosForm
    template_name = 'pedidos/pedidos_form.html'
    success_url = reverse_lazy('pedidos_listar')

class PedidosDelete(DeleteView):
    model = Pedidos
    template_name = 'pedidos/pedidos_delete.html'
    success_url = reverse_lazy('pedidos_listar')

