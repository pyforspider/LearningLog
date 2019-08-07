import os

from django.http import HttpResponse
from django.shortcuts import render

from App.models import UserModel


def index(request):
	return render(request, 'index.html')


def upload_file(request):
	if request.method == 'GET':
		return render(request, 'index.html')
	elif request.method == 'POST':
		image = request.FILES.get('image')
		print(type(image))
		with open('E:\\pyforspider\\mywebsite\\Day05\\SqlToModel\\static\\img\\picture.jpg', 'wb') as fb:
			for part in image.chunks():
				fb.write(part)
				fb.flush()
		return HttpResponse('上传成功')


def image_field(request):
	if request.method == 'GET':
		return render(request, 'image_field.html')
	elif request.method == 'POST':
		username = request.POST.get('username')
		image = request.FILES.get('image')
		user = UserModel()
		user.u_name = username
		user.u_icon = image
		user.save()
		return HttpResponse('上传成功')


def mine(request):
	username = request.GET.get('username')  # 这里的username仅仅只是从url获取的名字

	user = UserModel.objects.get(u_name=username)
	print('/static/upload/' + user.u_icon.url)
	img_url = '/static/upload/' + user.u_icon.url

	# return HttpResponse('获取图片成功')
	context = {
		'username': user.u_name,
		'img_url': img_url
	}
	return render(request, 'mine.html', context=context)