from django.shortcuts import render
from .models import *
from person.models import *
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
import PyPDF2

class Home(ListView):
    model = Material
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['teach_list'] = Teach.objects.all()
        return context
    
class MaterialList(ListView):
    model = Material
    
    
class MaterialDetail(DetailView):
    model = Material

    
    
