from django.http import HttpResponse
from django.shortcuts import render

from Two.models import Person, IDCard, Customer, Goods, Dog, Cat


def hello(request):
	return HttpResponse('hello')


def add_person(request):

	username = request.GET.get('username')
	person = Person()
	person.p_name = username
	person.save()

	return HttpResponse('Person创建成功 %s' % person.id)


def add_idcard(request):

	id_num = request.GET.get('idnum')
	print(id_num)
	id_card = IDCard()
	id_card.id_num = id_num
	id_card.save()

	return HttpResponse('IDCard创建成功 %s' % id_card.id)


def bind_card(request):

	person = Person.objects.last()
	idcard = IDCard.objects.last()
	idcard.id_person = person
	idcard.save()
	return HttpResponse('绑定成功')


def remove_person(request):
	person = Person.objects.last()
	person.delete()
	return HttpResponse('人员移除成功')


def remove_idvard(request):
	id_card = IDCard.objects.last()
	id_card.delete()
	return HttpResponse('身份证移除成功')


def get_idcard(request):
	person = Person.objects.last()
	idcard = person.idcard               # 隐形属性 即 模型名称小写
	return HttpResponse(idcard.id_num)


def get_person(request):
	idcard = IDCard.objects.last()
	person = idcard.id_person
	return HttpResponse(person.p_name)


def add_customer(request):
	c_name = request.GET.get('cname')
	customer = Customer()
	customer.c_name = c_name
	customer.save()

	return HttpResponse('%s消费者创建成功' % customer.c_name)


def add_goods(request):
	g_name = request.GET.get('gname')
	goods = Goods()
	goods.g_name = g_name
	goods.save()

	return HttpResponse('%s 商品创建成功' % goods.g_name)


def add_to_cart(request):
	customer = Customer.objects.last()
	goods = Goods.objects.last()
	print(type(goods.g_customer))
	# goods.g_customer.add(customer)   #绑定的两种方法都可行
	customer.goods_set.add(goods)

	return HttpResponse('绑定成功')


def get_goods_list(request, customer_id):
	customer = Customer.objects.get(pk=customer_id)
	goodslist = customer.goods_set.all()
	for goods in goodslist:
		print(goods.g_name)
	return HttpResponse('获取成功')


def add_dog(request):
	dog = Dog()
	dog.a_name = 'Dog1'
	dog.save()
	return HttpResponse('Dog创建成功 %s' % dog.id)


def add_cat(request):
	cat = Cat()
	cat.a_name = 'Cat1'
	cat.c_food = 'fish'
	cat.save()
	return HttpResponse('Cat创建成功 %s' % cat.id)


def get_dog(request):
	dog = Dog.objects.get(animal_ptr_id=11)
	print(dog.a_name)
	return HttpResponse('获取成功')