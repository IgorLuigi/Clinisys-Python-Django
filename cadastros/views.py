from django.shortcuts import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from models import Cidade, Funcionario, Paciente, Agenda, Consulta

# Create your views here.

########################### CREATE VIEW ###########################

class Index(TemplateView):
    template_name = 'cadastros/index.html'

class CidadeCreate(CreateView):
    model = Cidade
    tempalte_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

########################### DELETE VIEW ###########################

class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'cadastros/form=delete.html'
    success_url = reverse_lazy('index')

########################### LIST VIEW ###########################

class CidadeList(ListView):
    model = Cidade
    template_name = 'cadastros'