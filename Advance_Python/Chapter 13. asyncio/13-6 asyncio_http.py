# asyncio 么有提供http协议接口 aiohttp

import asyncio
import socket
import time
from urllib.parse import urlparse


async def get_url(url):
	# 通过socket请求html
	url = urlparse(url)
	host = url.netloc
	path = url.path
	if path == "":
		path = '/'
	# print(host, path)

	# 建立socket链接
	reader, writer = await asyncio.open_connection(host, 80)
	writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
	all_lines = []
	async for raw_line in reader:
		data = raw_line.decode("utf8")
		all_lines.append(data)
	html = "\n".join(all_lines)
	return html


if __name__ == '__main__':
	start_time = time.time()
	loop = asyncio.get_event_loop()
	tasks = []
	for url in range(3, 4):
		url = 'http://shop.projectsedu.com/goods/{}/'.format(url)
		# tasks.append(get_url(url))
		tasks.append(asyncio.ensure_future(get_url(url)))
	loop.run_until_complete(asyncio.wait(tasks))
	for task in tasks:
		print(task.result())
	print('last time {}'.format(time.time()-start_time))






	# 建立socket链接
	# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# # client.setblocking(False)
	# client.connect((host, 80))  # 阻塞不会消耗cpu

	# 不停的许文连接是否建立好， 需要while循环不停的去检查状态
	# 做计算任务或者再次发起其他的链接请求
	# client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
