# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_auto_20170702_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='metro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Metro', verbose_name='\u041c\u0435\u0442\u0440\u043e'),
        ),
    ]
