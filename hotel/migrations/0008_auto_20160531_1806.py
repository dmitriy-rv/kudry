# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-31 15:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='name',
            new_name='title',
        ),
    ]
