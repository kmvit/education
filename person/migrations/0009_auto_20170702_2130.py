# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 21:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0008_person_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.City', verbose_name='\u0413\u043e\u0440\u043e\u0434'),
        ),
    ]
