import random
from io import BytesIO
from time import sleep

# from django.core.cache import cache
from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.core.cache import caches, cache
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from App.models import Student
from App.utils import generate_code, get_rgb_tuple, get_code_pic
from DjangoCache2 import settings


def index(request):

	return HttpResponse('index')


# @cache_page(30)  # 缓存失效时间
def news(request):

	cache = caches['redis_backend']
	result = cache.get('news')
	if result:
		return HttpResponse(result)

	news_list = []
	for i in range(10):
		news_list.append('最近贸易战又开始了%s' % i)

	sleep(5)

	response = render(request, 'news.html', context={'news_list': news_list})

	cache.set('news', response.content, timeout=30)

	return response


@cache_page(60, cache='default')
def jokes(request):
	sleep(5)
	return HttpResponse('joke_list')


def get_xm(request):
	return HttpResponse('恭喜抢到小米')


def get_phone(request):
	if random.randrange(0, 100) > 95:
		return HttpResponse('恭喜抢到手机')
	return HttpResponse('请再接再厉')


def get_ticket(request):
	return HttpResponse('恭喜抢到优惠卷')


def search(request):
	return HttpResponse('搜索成功')


def calc(request):
	a, b = 10, 20
	c = (a+b)/0
	return HttpResponse(c)


@csrf_exempt
def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	elif request.method == 'POST':
		code = request.POST.get('verifycode')
		code_s = request.session.get('code')
		if code.lower() == code_s.lower():
			return HttpResponse('POST登录成功')
		else:
			return HttpResponse('POST登录失败')


def add_student(request):
	for i in range(100):
		student = Student()
		student.s_name = '小明%s' % i
		student.save()
	return HttpResponse('学生批量创建成功')


def get_students(request):
	students = Student.objects.all()
	return render(request, 'student_list.html', context=locals())


def get_students_page(request):
	info_num = int(request.GET.get('info_num'))
	page_num = int(request.GET.get('page_num'))
	students = Student.objects.all()[info_num*(page_num-1): info_num*page_num]
	return render(request, 'student_list.html', context={'students': students})


def get_students_page2(request):
	per_page = int(request.GET.get('per_page', 10))
	page = int(request.GET.get('page', 1))      	# 不加参数时，第一个页面显示第一页
	students = Student.objects.all()

	paginator = Paginator(students, per_page)   	# 分页器实例化（QueryList, per_page）
	page_object = paginator.page(page)          	# 第（page）页的一个对象: page_object 有多个属性，如object_list
	page_range = paginator.page_range           	# 存储页码的列表 [页码]

	context = {
		'page_object': page_object,
		'page_range': page_range,
	}

	return render(request, 'student_list_paging_beauty.html', context=context)


def get_code(request):
	code = generate_code()
	request.session['code'] = code
	pic = get_code_pic(code)
	return HttpResponse(pic, content_type='image/png')
