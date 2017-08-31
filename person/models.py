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
        
class City(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    city = models.ForeignKey(Country, verbose_name='Страна')
    class Meta:
        verbose_name = 'Город'
    def __unicode__(self):
        return '%s' % (self.title)

class Metro(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    city = models.ForeignKey(City, verbose_name='Город')
    class Meta:
        verbose_name = 'Метро'
    def __unicode__(self):
        return '%s' % (self.title)
        
class Teach(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    class Meta:
        verbose_name = 'Предмет'
    def __unicode__(self):
        return '%s' % (self.title)

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', verbose_name='Аватар')
    fio = models.CharField(max_length=300, verbose_name='ФИО')
    age = models.IntegerField(verbose_name='Возраст')
    country = models.ForeignKey(Country, verbose_name='Страна')
    city = models.ForeignKey(City, verbose_name='Город')
    teacher = models.BooleanField(default=False, verbose_name='Преподователь')
    programm = models.CharField(max_length=300, verbose_name='Программа', default="Школьная")
    teach = models.ForeignKey(Teach, verbose_name='Предмет')
    price = models.IntegerField(verbose_name='Цена за час', default='500')
    material = models.CharField(max_length=1000, verbose_name='Материалы')
    metro = models.ForeignKey(Metro, verbose_name='Метро')
    goto_student = models.BooleanField(default=False, verbose_name='Выезд у ученику')
    class Meta:
        verbose_name = 'Персона'
    def __unicode__(self):
        return self.fio
        
        
