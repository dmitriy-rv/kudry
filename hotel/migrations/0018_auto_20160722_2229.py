# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-22 19:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0017_auto_20160721_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='date_from',
        ),
        migrations.RemoveField(
            model_name='date',
            name='date_to',
        ),
    ]
