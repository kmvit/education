# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_auto_20170421_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='exclusive',
            field=models.BooleanField(default=False, verbose_name='\u042d\u043a\u0441\u043a\u043b\u044e\u0437\u0438\u0432\u043d\u044b\u0439'),
        ),
    ]
