from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def hello(request):
	response = HttpResponse()
	response.content = "德玛西亚"
	# response.status_code = 404

	response.write('该刷马桶了')
	response.flush()

	response.content_type = 'image/apng'
	return response

	# return HttpResponse('该刷马桶了')


def get_ticket(request):

	# redirect(reverse('url get_ticket'))

	url = reverse('hello')

	# return HttpResponseRedirect('/app/hello/')
	# return HttpResponseRedirect(url)
	return redirect(url)


def get_info(request):

	info = {
		'status': 200,
		'msg': 'ok',
	}

	return JsonResponse(info)


def set_cookie(request):
	response = HttpResponse('设置Cookie')
	response.set_cookie('hobby', 'gaming', max_age=60)

	return response


def get_cookie(request):
	hobby = request.COOKIES.get('hobby')
	return HttpResponse(hobby)


def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	elif request.method == 'POST':
		response = HttpResponseRedirect(reverse('mine'))
		username = request.POST.get('user')
		# response.set_cookie('username', username, max_age=6)   # 注意这里的response一定要返回，否则cookie设置失败，因为没有返回
		response.set_signed_cookie('content', username, 'rock')
		return response
# return redirect(reverse('mine'))


def mine(request):
	try:
		username = request.get_signed_cookie('content', salt='rock')
		if username:
			return render(request, 'mine.html', context={'username':username})
	except:
		print('获取失败')
	return redirect(reverse('login'))


def logout(request):

	response = redirect(reverse('login'))
	response.delete_cookie('content')

	return response
