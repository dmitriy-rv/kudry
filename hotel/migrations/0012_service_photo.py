# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-08 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_serv_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='photo',
            field=models.BooleanField(default=False, verbose_name='\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u043e\u0442\u043e\u0430\u043b\u044c\u0431\u043e\u043c'),
        ),
    ]