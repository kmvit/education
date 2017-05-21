from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
import PyPDF2

class Home(ListView):
    model = Material
    template_name = 'index.html'
    
class MaterialList(ListView):
    model = Material
    
    
class MaterialDetail(DetailView):
    model = Material

    
    
   