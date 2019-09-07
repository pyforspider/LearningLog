# 生成器是可以暂停的函数

import inspect

# def gen_func():
# 	# 1. 返回值给调用方 2. 从调用方接收.send()值 --> 协程
# 	# value = yield 1
# 	value = yield from gen
# 	return "bobby"
# 1. 用同步的方式编写异步的代码，在适当的时候暂停函数并在适当的时候启动函数

import socket


def get_socket_data():
	yield "bobby"


def downloader(url):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.setblocking(False)
	try:
		client.connect((host, 80))
	except BlockingIOError:
		pass
	selector.register(client.fileno(), EVENT_WRITE, self.connected)
	source = yield from get_socket_data()
	data = source.decode("utf-8").split("\r\n\r\n")[1]
	print(data)


def download_html(url):
	# select 事件循环监听 yield from 是否准备完毕
	# 协程的调度依然是  事件循环+协程模式  协程是单线程模式
	html = yield from downloader(url)


if __name__ == "__main__":
	gen = gen_func()
	print(inspect.getgeneratorstate(gen))
	next(gen)
	print(inspect.getgeneratorstate(gen))
	try:
		next(gen)
	except StopIteration:
		pass
	print(inspect.getgeneratorstate(gen))