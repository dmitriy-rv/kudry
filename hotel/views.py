### -*- coding: utf-8 -*- ###


from django.shortcuts import render
from django.template import loader, Context
from django.http import Http404, HttpRequest, HttpResponseRedirect, HttpResponse, JsonResponse
from django.db.models import Q
from django.core.mail import send_mail

# Create your views here.

from django.shortcuts import render_to_response
from hotel.models import Action, Articles, Room, Image, Reviews, Service, Serv_Image, Room_ind, Date
from django.contrib.auth.models import User, Group

def main(request):
	action = Action.objects.all().order_by("-id")
	content = Articles.objects.filter(id=1)
	service = Service.objects.filter(main=True)
	return render_to_response('main.html',
    	{'action':action,
    	'text':content,
    	'service':service, 
    	'map':True}
    )

def action(request, offset):
	article = Action.objects.filter(id=offset)
	return render_to_response(
		'base.html',
		{'article':article}
	)

def rooms(request):
	room = Room.objects.all().order_by("id")
	image = Image.objects.all()
	return render_to_response('rooms.html',
		{'room':room,
		'images':image}
	)

def about(request):
	content = Articles.objects.filter(id=2)
	return render_to_response(
		'base.html',
		{'article':content,
		'map':True}
	)

def reviews(request):
	reviews = Reviews.objects.all()
	return render_to_response(
		'reviews.html',
		{'reviews':reviews,
		'message':False}
	)

def service(request):
	service = Service.objects.all()
	return render_to_response(
		'service.html',
		{'service':service}
	)

def one_service(request, offset):
	article = Service.objects.filter(id=offset)
	images = Serv_Image.objects.filter(title_id=offset)
	return render_to_response(
		'base.html',
		{'article':article,
		'images':images}
	)

def send_review(request):
	if request.GET:
		from models import Reviews
 		b = Reviews(name=request.GET['name'], date_from=request.GET['date_from'] ,date_to=request.GET['date_to'] , text=request.GET['text'])
 		b.save()

 	reviews = Reviews.objects.all()
	send = u'Постоялец '+request.GET['name']+u' оставил комментарий с текстом:\n'+ request.GET['text']
	send_mail('Комментарий на сайте "Кудры"', send, 'atlasgzw@atlas-gagra.ru', ['dimarikrv@gmail.com'], fail_silently=False)

 	return render_to_response(
		'reviews.html',
		{'reviews':reviews,
		'message':True}
	)


def admin_service(request):
	if request.user.is_authenticated():
		service = Service.objects.all()
		user = User.objects.filter(groups__name='Турфирмы')

		return render_to_response('admin/admin_service.html')
	else:
 		return HttpResponseRedirect("/admin/login/")



def admin_take_data(request):
	rooms = Room_ind.objects.all()
	date = Date.objects.all()
	room_type = Room.objects.all()
	user = User.objects.filter(groups__name='Турфирмы')

	send = []
	send_rooms = []
	send_room_type = []
	send_tenants = []
	send_firm = []

	for item in rooms:
		send_rooms.append({'number':item.number, 'stat':item.stat, 'room_type':item.room_type.title})

	for item in user:
		send_firm.append({'name':item.first_name})

	for item in date:

		send_tenants.append({
			'number':item.number.number,
			'tenant':item.surname,
			'tenant_id':item.id,
			'first_name':item.first_name,
			'second_name':item.second_name,
			'date_bdh':item.date_birthday,
			'firm':item.firm,
			'pass':item.pass_data,
			'date_from':item.date_from,
			'date_to':item.date_to
			})

	for item in room_type:
		send_room_type.append({'name':item.title,'id':item.id})

	send.append(send_rooms)
	send.append(send_tenants)
	send.append(send_room_type)
	send.append(send_firm)

	return JsonResponse(send, safe=False)

def admin_manage_number(request):
	room = 'bad'	

	if request.GET:

		if request.GET['option'] == '1':			
			if request.GET['stat'] == u"Работает":
				stat = 'avaible'
			else:
				stat = 'disable'

			item = Room_ind(
				number = request.GET['number'],
				stat = stat,
				room_type = Room.objects.get(id = int(request.GET['type']))
			)

			item.save()

			room = 'Номер успешно создан!'

		if request.GET['option'] == '2':			
			if request.GET['stat'] == u"Работает":
				stat = 'avaible'
			else:
				stat = 'disable'
			
			item = Room_ind.objects.get(number = request.GET['number'])

			item.stat = stat
			item.room_type = Room.objects.get(id = int(request.GET['type']))

			item.save()

			room = 'Номер успешно изменен!'

		if request.GET['option'] == '3':
			item = Room_ind.objects.get(number=request.GET['number'])
			item.delete()	

			room = 'Номер успешно удален!'
	
	return JsonResponse({'room':room}, safe=False)


def admin_manage_tenant(request):
	status = 'bad'

	if request.GET:

		if request.GET['option'] == '1':			
			
			item = Date(
				number = Room_ind.objects.get(number = request.GET['number']),
				surname = request.GET['surname'],
				first_name = request.GET['first_name'],
				second_name = request.GET['second_name'],
				date_birthday = request.GET['date_birthday'],
				pass_data = request.GET['pass_data'],
				firm = request.GET['firm'],
				date_from = request.GET['date_from'],
				date_to = request.GET['date_to'],
			)

			item.save()

			status = 'Жилец успешно добавлен!'

		if request.GET['option'] == '2':

			item = Date.objects.get(id = request.GET['id'])
			item.number = Room_ind.objects.get(number = request.GET['number'])
			item.surname = request.GET['surname']
			item.first_name = request.GET['first_name']
			item.second_name = request.GET['second_name']
			item.date_birthday = request.GET['date_birthday']
			item.pass_data = request.GET['pass_data']
			item.firm = request.GET['firm']
			item.date_from = request.GET['date_from']
			item.date_to = request.GET['date_to']
			
			item.save()

			status = 'Жилец успешно изменен!'

		if request.GET['option'] == '3':
			item = Date.objects.get(id=request.GET['tenant'])
			item.delete()

			status = 'Жилец успешно удален!'

	return JsonResponse({'status':status}, safe=False)