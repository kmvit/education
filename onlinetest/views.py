from .models import *
from materials.models import *
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

class TestList(ListView):
    model = Quiz
    
    
class TestDetail(DetailView):
    model = Quiz
    def get_context_data(self, **kwargs):
        context = super(TestDetail, self).get_context_data(**kwargs)
        context['material_list'] = Material.objects.all()
        context['question_list'] = Question.objects.filter(quiz = self.kwargs['pk'])
        return context
        
class QuestionDetail(DetailView):
    model = Question
    def get_object(self):
        return get_object_or_404(Question, id=self.kwargs['question_pk'])
    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        context['quiz'] = get_object_or_404(Quiz, id=self.kwargs['pk'])
        context['material_list'] = Material.objects.all()
        return context 