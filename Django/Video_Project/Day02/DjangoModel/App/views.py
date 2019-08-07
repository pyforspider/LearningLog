import random

from django.http import HttpResponse
from django.shortcuts import render

from App.models import Person


def index(request):
	return HttpResponse('')


def add_persons(request):

	for i in range(15):
		person = Person()
		flag = random.randrange(100)
		person.p_name = 'Tom%s' % i
		person.p_age = flag
		person.p_sex = flag % 2
		person.save()

	return HttpResponse('批量创建成功。')


def get_persons(request):

	# persons = Person.objects.filter(p_age__gt=50).filter(p_age__lt=80)
	# persons = Person.objects.exclude(p_age__lt=50).filter(p_age__lt=80)
	#
	# print(type(persons))
	#
	# persons_two = Person.objects.filter(p_age__in=[50, 57, 55])
	#
	# print(type(persons_two))

	persons = Person.objects.order_by('-id')
	persons_values = persons.values()

	print(type(persons_values))
	for persons_value in persons_values:
		print(persons_value)

	context = {
		'persons': persons
	}
	return render(request, 'person_list.html', context=context)


def add_person(request):
	# person = Person.objects.create(p_name='Sunkerr', p_age=15, p_sex=True)
	person = Person.create(p_name='Jacky')
	person.save()
	return HttpResponse('Scunk创建成功')


def get_person(request):

	person = Person.objects.get(p_age=100)
	# person = Person.objects.first()
	print(person.p_name)

	return HttpResponse('获取成功')