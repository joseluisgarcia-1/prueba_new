from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from apps.tipo.models import Objetivos, Receta
from apps.tipo.forms import ObjetivosForm, RecetaForm


def index_tipo(request):
    return HttpResponse("Soy la pagina principal de la app tipo")


class RecetaList(ListView):
    model = Receta
    template_name = 'tipo/tipo_list.html'

class RecetaCreate(CreateView):
    model = Receta
    template_name = 'tipo/tipo_form.html'
    form_class = RecetaForm
    second_form_class = ObjetivosForm
    success_url = reverse_lazy('tipo_listar')

    def get_context_data(self, **kwargs):
        context = super(RecetaCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.get_form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            plato = form.save(commit=False)
            plato.descripcion = form2.save()
            plato.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class RecetaUpdate(UpdateView):
    model = Receta
    second_model = Objetivos
    template_name = 'tipo/tipo_form.html'
    form_class = RecetaForm
    second_form_class = ObjetivosForm
    success_url = reverse_lazy('tipo_listar')

    def get_context_data(self, **kwargs):
        context = super(RecetaUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        plato = self.model.objects.get(id=pk)
        descripcion = self.second_model.objects.get(id=plato.descripcion_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=descripcion)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_plato = kwargs['pk']
        plato = self.model.objects.get(id=id_plato)
        descripcion = self.second_model.objects.get(id=plato.descripcion_id)
        form = self.form_class(request.POST, instance=plato)
        form2 = self.second_form_class(request.POST, instance=plato)
        if form.is_valid and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_succes_url())
        else:
            return HttpResponseRedirect(self.get_succes_url())

class RecetaDelete(DeleteView):
    model = Receta
    template_name = 'tipo/tipo_delete.html'
    success_url = reverse_lazy('tipo_listar')



