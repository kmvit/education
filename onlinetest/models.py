# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime

class Quiz(models.Model):
    title = models.CharField(max_length=400, verbose_name='Название', default ='1')
    created = models.DateField(default=datetime.date.today, verbose_name='Дата создания')
    class Meta:
        verbose_name='Тесты'
    def __unicode__(self):
        return self.title
    

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, verbose_name='Тест')
    title = models.CharField(max_length=400, verbose_name='Название', default ='1')
    class Meta:
        verbose_name='Вопросы'
    def __unicode__(self):
        return self.title
    
        
class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name='Вопрос')
    title = models.CharField(max_length=400, verbose_name='Название')
    is_valid = models.BooleanField(default=False)
    class Meta:
        verbose_name='Ответы'
    def __unicode__(self):
        return self.title
    
