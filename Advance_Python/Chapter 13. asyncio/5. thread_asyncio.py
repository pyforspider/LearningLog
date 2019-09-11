# 使用多线程: 在协程中集成阻塞io

import asyncio
import socket
import time
from concurrent.futures.thread import ThreadPoolExecutor
from urllib.parse import urlparse


def get_url(url):
	url = urlparse(url)
	path = url.path
	host = url.netloc
	if path == "":
		path = "/"

	# client 为固定写法
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((host, 80))
	# http 的 send() 方法固定写法：
	client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
	data = b""
	while True:
		d = client.recv(1024)
		if d:
			data += d
		else:
			break
	client.close()
	print(data.decode("utf-8").split("\r\n\r\n")[1])
	return data.decode("utf-8").split("\r\n\r\n")[1]


if __name__ == '__main__':
	start_time = time.time()
	loop = asyncio.get_event_loop()
	# 声明一个线程池, 可以加入限制线程数
	executor = ThreadPoolExecutor()
	# loop.run_in_executor(executor, func_name, func_args)
	# loop.run_in_executor(executor, get_url, "http://www.imooc.com")
	tasks = []
	for i in range(2, 20):
		url = "http://shop.projectsedu.com/goods/{}/".format(i)
		# loop.run_in_executor(executor, func_name, func_args)返回的是 task 对象
		task = loop.run_in_executor(executor, get_url, url)
		tasks.append(task)
	loop.run_until_complete(asyncio.wait(tasks))
	print("last time :{}".format(time.time()-start_time))



