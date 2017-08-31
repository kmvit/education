# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from .models import *
# Create your views here.

class SearchTeacher(ListView):
    model = City
    template_name='person/search.html'
    def get_context_data(self, **kwargs):
        context = super(SearchTeacher, self).get_context_data(**kwargs)
        context['teach_list'] = Teach.objects.all()
        context['metro_list'] = Metro.objects.all()
        return context
    
    
class SearchResult(ListView):
    model = Person
    template_name = 'person/person_search_results.html'
    def get_queryset(self, **kwargs):
        if 'optionsRadios' in self.request.GET and 'gotostudent' in self.request.GET:
            return Person.objects.filter(teach__title=self.request.GET['selectType'], metro=self.request.GET['optionsRadios'], goto_student=self.request.GET['gotostudent'], price__gte=self.request.GET['selectPrice'], price__lte=self.request.GET['selectPrice2'])
        elif 'optionsRadios' in self.request.GET:
            return Person.objects.filter(teach__title=self.request.GET['selectType'], metro=self.request.GET.getlist('optionsRadios'), price__gte=self.request.GET['selectPrice'], price__lte=self.request.GET['selectPrice2'])
        elif 'selectType' in self.request.GET:
            return Person.objects.filter(teach__title=self.request.GET['selectType'], price__gte=self.request.GET['selectPrice'], price__lte=self.request.GET['selectPrice2'])
        else:
            return Person.objects.filter(teach__title=self.request.GET['selectType'], goto_student=self.request.GET['gotostudent'], price__gte=self.request.GET['selectPrice'], price__lte=self.request.GET['selectPrice2'])

