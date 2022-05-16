from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from models import Cidade, Pessoa

# Create your views here.
class Index(TemplateView):
    template_name = 'paginas/index.html'





#################### DELETE VIEWS ###############################

class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'cadastros/form-delete.html'
    sucess_url = reverse_lazy('index')


class PessoaDelete(DeleteView):
    model = Pessoa
    template_name = 'cadastros/form-delete.html'
    sucess_url = reverse_lazy('index')


#################################################################

class CidadeList(ListView):
    model = Cidade
    template_name = 'cadastros'







