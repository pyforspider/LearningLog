import hashlib
import random
import time

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from Two.models import User


def index(request):
	response = HttpResponse('index')

	return response


def login(request):
	if request.method == 'GET':
		return render(request, 'two_login.html')
	elif request.method == 'POST':
		user = request.POST.get('user')
		request.session['user'] = user     # 存储在字典？？  还是基于 cookie的
		return HttpResponse('登录成功')


def mine(request):

	user = request.session.get('user')

	return render(request, 'two_mine.html', context=locals())


def logout(request):

	response = redirect(reverse('mine'))

	# response.delete_cookie('sessionid')
	# del request.session['user']   # 这种方法第一次删除正常，第二次由于数据库的值不完整，会报错
	request.session.flush()

	return response


def register(request):
	if request.method == 'GET':
		return render(request, 'register.html')    # 注意表单提交要声明 方式 method='post'
	elif request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		try:
			user = User()
			user.u_name = username
			user.u_password = password
			user.save()
		except Exception as e:
			return redirect(reverse('register'))
	return HttpResponse('注册成功')


# @csrf_exempt
def user_login(request):
	if request.method == 'GET':
		return render(request, 'user_login.html')
	elif request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		# username = request.GET.get('username')   # test client 模拟测试移动端时使用GET
		# password = request.GET.get('password')
		users = User.objects.all().filter(u_name=username).filter(u_password=password)
		if users.exists():
			user = users.first()
			token = random.randrange(1, 1000)
			user.u_token = token
			user.save()

			# 浏览器
			# response = HttpResponse('用户登录成功')        # token精华部分 在用户登录时，使用token设置一个Cookie
			# response.set_cookie('token', token)
			# return response

			# 移动端
			data = {
				'status': 200,
				'msg': '登录成功',
				'token': token,
			}
			return JsonResponse(data=data)

	# 浏览器
	# return redirect(reverse('user_login'))

	# 移动端
	data = {
		'status': 800,
		'msg': '登录失败',
	}
	return JsonResponse(data=data)


def generate_token(ip, username):
	c_time = time.ctime()
	r = username
	return hashlib.new('md5', (ip + c_time + r).encode('utf-8')).hexdigest()


def user_mine(request):

	# token = request.COOKIES.get('token')               # 从 cookie 取用 token
	token = request.GET.get('token')
	try:
		user = User.objects.get(u_token=token)
	except Exception as e:
		return redirect(reverse('user_login'))

	# return render(request, 'user_mine.html', context={'username': user.u_name})
	data = {
		'status': 200,
		'msg': 'ok',
		'data': {
			'username': user.u_name,
		}
	}
	return JsonResponse(data=data)
