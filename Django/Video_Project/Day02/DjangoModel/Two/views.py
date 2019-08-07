from django.db.models import Max, Avg, F, Q
from django.http import HttpResponse
from django.shortcuts import render


from Two.models import User, Order, Grade, Custom, Company, Animal


def get_user(request):

	username = 'Sunck'
	password = '120'

	users = User.objects.filter(u_name=username)
	print(users.count())
	# if users.count():
	if users.exists():
		user = users.first()
		if user.u_password == password:
			print('用户信息获取成功')
		else:
			print('密码错误')
	else:
		print('用户不存在')

	return HttpResponse('获取成功')


def get_users(request):

	users = User.objects.all()[1:5]
	print(users)
	print(type(users))
	for user in users:
		print(user.u_name)
	context = {
		'users': users
	}
	return render(request, 'user_list.html', context=context)


def get_order(request):
	orders = Order.objects.filter(o_time__month=8)
	for order in orders:
		print(order.o_num)

	return HttpResponse('获取订单成功')


def get_grade(request):

	grade = Grade.objects.filter(student__s_name='Jack')
	print(grade.first().g_name)

	return HttpResponse('获取成功')


def get_custom(request):

	result = Custom.objects.aggregate(Avg('c_cost'))
	print(result)
	return HttpResponse('获取花费超过')


def get_company(request):

	# companys = Company.objects.filter(c_girl_num__gt=F('c_boy_num') + 15)
	companies = Company.objects.filter(Q(c_boy_num__gt=1) & Q(c_girl_num__gt=20))

	for company in companies:
		print(company.c_name)

	return HttpResponse('获取公司成功')


def get_animals(request):

	animals = Animal.objects.all()
	for animal in animals:
		print(animal.a_name)

	animal_1 = Animal.objects.create()
	animal_1.save()
	print(animal_1.a_name)

	return HttpResponse('动物获取成功')
