import random
import time

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LearnMiddleware(MiddlewareMixin):

	def process_request(self, request):
		ip = request.META.get('REMOTE_ADDR')
		print('请求的IP地址：', ip, request.path)

		# if request.path == '/app/getphone/':
		# 	if ip == '127.0.0.1':
		# 		if random.randrange(0, 100) > 20:
		# 			return HttpResponse('VIP，恭喜你抢到手机了')
		#
		# if request.path == '/app/getticket/':
		# 	if ip.startswith('10.0.127.7'):
		# 		return HttpResponse('黑名单抢卷失败')
		#
		# if request.path == '/app/search/':
		# 	result = cache.get('ip')
		# 	if result:
		# 		return HttpResponse('请求过于频繁')
		# 	cache.set('ip', 'ip', timeout=10)

		black_list = cache.get('black', [])
		if ip in black_list:
			return HttpResponse('对不起，你已在黑名单中，禁止访问本网站')

		requests = cache.get(ip, [])
		if requests and time.time() - requests[-1] > 60:     # 弹出列表中 超过60s 的时间戳
			requests.pop()
		requests.insert(0, time.time())                       # 列表插入时间戳 insert(index, content)
		cache.set(ip, requests)                               # 当前缓存插入列表

		if len(requests) > 6000:                               # 列表时间戳数量大于30 时
			black_list.append(ip)
			cache.set('black', black_list, timeout=60)
			return HttpResponse('请求过于频繁，黑名单见')

		if len(requests) > 600:                               # 列表时间戳数量大于10 时
			return HttpResponse('请求过于频繁，小爬虫回家睡觉吧')

	# def process_exception(self, request, exception):
	# 	return redirect(reverse('get_xm'))


class TwoMiddleware(MiddlewareMixin):

	def process_request(self, request):
		print('Two Middleware')
