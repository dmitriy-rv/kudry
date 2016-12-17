### -*- coding: utf-8 -*- ###

from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from image_cropping import ImageRatioField

# Create your models here.
class Articles(models.Model):
	title = models.CharField(max_length=30, verbose_name='Заголовок')
	text = RichTextUploadingField(verbose_name='Содержание')

	def __unicode__(self):
		return self.title

class Action(models.Model):
	title = models.CharField(max_length=30, verbose_name='Заголовок')
	main_text = models.CharField(max_length=100, verbose_name='Анонс на главную')
	main_img = models.ImageField(upload_to='./img', verbose_name='Изображение на главную')
	cropping = ImageRatioField('main_img', '1200x350', allow_fullsize=True)
	text = RichTextUploadingField(verbose_name='Основной текст')

	def __unicode__(self):
		return self.title


class Room(models.Model):
	title = models.CharField(max_length=30, verbose_name='Заголовок')
	text = RichTextUploadingField(verbose_name='Описание')
	may = models.IntegerField(verbose_name='Май')
	june = models.IntegerField(verbose_name='Июнь')
	july = models.IntegerField(verbose_name='Июль')
	august = models.IntegerField(verbose_name='Август')
	september = models.IntegerField(verbose_name='Сентябрь')
	october = models.IntegerField(verbose_name='Октябрь')
	other = models.IntegerField(verbose_name='Ноябрь-Апрель')

	def __unicode__(self):
		return self.title

class Image(models.Model):
	title = models.ForeignKey(Room)
	images = models.ImageField(upload_to='./img', verbose_name='Фотографии')

class Reviews(models.Model):
	name = models.CharField(max_length=30, verbose_name='Имя')
	date_from = models.DateField( verbose_name='Дата заезда')
	date_to = models.DateField( verbose_name='Дата выезда')
	text = RichTextUploadingField(verbose_name='Отзыв')
	allow = models.BooleanField(default=False, blank=True,  verbose_name='Опубликовать')  

	def __unicode__(self):
		if self.allow == True:
			return self.name+"..........Одобрен"
		if self.allow == False:
			return self.name+"..........НЕ ОДОБРЕН!"

class Service(models.Model):
	title = models.CharField(max_length=30, verbose_name='Название')
	main_text = models.TextField(verbose_name='Текст на страницу услуг') 
	main_img = models.ImageField(upload_to='./img', verbose_name='Изображение на страницу услуг')
	cropping = ImageRatioField('main_img', '350x235', allow_fullsize=True)
	more = models.BooleanField(default=False, blank=True,  verbose_name='Подробнее') 
	main = models.BooleanField(default=False, blank=True,  verbose_name='На главную') 
	text =RichTextUploadingField(blank=True, verbose_name='Подробный текст')
	photo = models.BooleanField(default=False, blank=True,  verbose_name='Добавить фотоальбом') 

	def __unicode__(self):
		return self.title


class Serv_Image(models.Model):
	title = models.ForeignKey(Service)
	images = models.ImageField(upload_to='./img', verbose_name='Фотографии')

stat_type = (
    ('avaible', 'Работает'),
    ('disable', 'Не работает'),
)

class Room_ind(models.Model):
	number = models.CharField(max_length=5, verbose_name='№ номера')
	stat = models.CharField(max_length=20, choices=stat_type, verbose_name='Статус')
	room_type = models.ForeignKey(Room)

class Date(models.Model):
	number = models.ForeignKey(Room_ind)
	surname = models.CharField(max_length=30, verbose_name='Фамилия')
	first_name = models.CharField(max_length=30, verbose_name='Имя')
	second_name = models.CharField(max_length=30, verbose_name='Отчество')		
	date_birthday = models.DateField( verbose_name='Дата рождения')
	pass_data = models.TextField( verbose_name='Паспорт') 
	firm = models.CharField(max_length=30, verbose_name='Турфирма') 
	date_from = models.DateField( verbose_name='Дата заезда')
	date_to = models.DateField( verbose_name='Дата выезда')