# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-07 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_service_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Room_ind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5, verbose_name='\u2116 \u043d\u043e\u043c\u0435\u0440\u0430')),
                ('stat', models.CharField(choices=[('\u0417\u0430\u043d\u044f\u0442', '\u0417\u0430\u043d\u044f\u0442'), ('\u0421\u0432\u043e\u0431\u043e\u0434\u0435\u043d', '\u0421\u0432\u043e\u0431\u043e\u0434\u0435\u043d'), ('\u041d\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442', '\u041d\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442')], max_length=20, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Tenants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
