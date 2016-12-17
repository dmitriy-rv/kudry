# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-21 02:09
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_action_cropping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='./img', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='\u0422\u0438\u043f \u0436\u0438\u043b\u044c\u044f')),
                ('room_type', models.CharField(choices=[('\u042d\u043a\u043e\u043d\u043e\u043c', '\u042d\u043a\u043e\u043d\u043e\u043c'), ('\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442', '\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442'), ('\u041f\u043e\u043b\u0443\u043b\u044e\u043a\u0441', '\u041f\u043e\u043b\u0443\u043b\u044e\u043a\u0441'), ('\u041b\u044e\u043a\u0441', '\u041b\u044e\u043a\u0441')], max_length=20, verbose_name='\u0422\u0438\u043f \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('may', models.IntegerField(verbose_name='\u041c\u0430\u0439')),
                ('june', models.IntegerField(verbose_name='\u0418\u044e\u043d\u044c')),
                ('july', models.IntegerField(verbose_name='\u0418\u044e\u043b\u044c')),
                ('august', models.IntegerField(verbose_name='\u0410\u0432\u0433\u0443\u0441\u0442')),
                ('other', models.IntegerField(verbose_name='\u0421\u0435\u043d\u0442\u044f\u0431\u0440\u044c-\u0410\u043f\u0440\u0435\u043b\u044c')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Room'),
        ),
    ]
