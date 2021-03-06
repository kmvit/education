# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_remove_person_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Country', verbose_name='\u0421\u0442\u0440\u0430\u043d\u0430')),
            ],
        ),
        migrations.CreateModel(
            name='Metro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.City', verbose_name='\u0413\u043e\u0440\u043e\u0434')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='metro',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='person.Metro', verbose_name='\u041c\u0435\u0442\u0440\u043e'),
        ),
    ]
