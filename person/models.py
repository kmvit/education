# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Country(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    class Meta:
        verbose_name = 'Страна'
    def __unicode__(self):
        return '%s' % (self.title)

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fio = models.CharField(max_length=300, verbose_name='ФИО')
    age = models.IntegerField(verbose_name='Возраст')
    country = models.ForeignKey(Country, verbose_name='Страна')
    teacher = models.BooleanField(default=False, verbose_name='Преподователь')
    teach = models.CharField(max_length=1000, verbose_name='Занятия')
    material = models.CharField(max_length=1000, verbose_name='Материалы')
    class Meta:
        verbose_name = 'Персона'
    def __unicode__(self):
        return self.fio
        
        
