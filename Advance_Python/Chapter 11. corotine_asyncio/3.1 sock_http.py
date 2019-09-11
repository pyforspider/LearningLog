# 1. epoll并不一定比 select好
# 2. 在并发度高，连接不活跃时，epoll好， 如 网页
# 3. 在连接活跃，并发度不高时， select好， 如 游戏

import socket
import time
from urllib.parse import urlparse


# 通过非阻塞io实现http请求, 但是一直处于不停询问连接
def get_url(url):
	url = urlparse(url)
	path = url.path
	host = url.netloc
	if path == "":
		path = "/"

	# client 为固定写法
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.setblocking(False)
	try:
		client.connect((host, 80))
	except BlockingIOError:
		pass

	# 不停地询问连接是否建立好， 需要while循环不停地去检查状态
	# 做计算任务或者发起其他请求
	while True:
		try:
			client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
			break
		except OSError:
			pass

	data = b""
	while True:
		try:
			d = client.recv(1024)
			if d:
				data += d
				continue
			else:
				break
		except OSError:
			pass
	client.close()
	return data.decode("utf-8").split("\r\n\r\n")[1]


if __name__ == '__main__':
	# html = get_url("http://www.baidu.com")
	# print(html)

	start_time = time.time()
	for i in range(20):
		url = "http://shop.projectsedu.com/goods/{}/".format(i)
		html = get_url(url)
		print(html)
	print("last time: {}".format(time.time()-start_time))
