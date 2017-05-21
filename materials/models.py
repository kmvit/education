# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Material(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    img = models.ImageField(upload_to='material', verbose_name='Изображение')
    body = models.TextField(verbose_name='Содержание')
    file = models.FileField(upload_to='material/files', verbose_name='Файлы')
    on_off = models.BooleanField(default=False, verbose_name='Платный')
    class Meta:
        verbose_name = 'Материалы'
    def __unicode__(self):
        return '%s' % (self.title)