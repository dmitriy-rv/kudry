# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-22 20:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0018_auto_20160722_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='name',
        ),
        migrations.RemoveField(
            model_name='date',
            name='number',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_type',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
    ]