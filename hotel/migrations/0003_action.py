# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-21 01:31
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20160520_0428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('main_text', models.CharField(max_length=100, verbose_name='\u0410\u043d\u043e\u043d\u0441 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u0443\u044e')),
                ('main_img', models.ImageField(upload_to='./img', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u0443\u044e')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0442\u0435\u043a\u0441\u0442')),
            ],
        ),
    ]
