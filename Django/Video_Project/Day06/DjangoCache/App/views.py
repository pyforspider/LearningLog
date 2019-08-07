from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
	return HttpResponse('hello')


def news(request):

	data = {
		'news': '贸易战开始了',
	}
	return render(request, 'news.html', context=data)
