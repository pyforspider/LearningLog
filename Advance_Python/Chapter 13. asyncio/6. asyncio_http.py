# asyncio 没有提供http协议接口. 如需使用aiohttp

import asyncio
import time
from urllib.parse import urlparse


# 同步的方式完成 html请求
async def get_url(url):
	url = urlparse(url)
	host = url.netloc
	path = url.path
	if path == "":
		path = '/'

	# asyncio 提供了 asyncio.open_connection() 协程
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
	for url in range(1, 20):
		url = 'http://shop.projectsedu.com/goods/{}/'.format(url)
		# tasks.append(get_url(url))
		# 获取结果, 将future放入 tasks 列表中
		future = asyncio.ensure_future(get_url(url))
		tasks.append(future)
	loop.run_until_complete(asyncio.wait(tasks))
	for future in tasks:
		print(future.result())
	print('last time {}'.format(time.time()-start_time))

"""
# 拓展：
# 下面使用了 asyncio.as_completed() 方法，使得完成一个任务打印一个任务. 此方法不必使用future
async def main():
	tasks = []
	for url in range(1, 20):
		url = 'http://shop.projectsedu.com/goods/{}/'.format(url)
		tasks.append(get_url(url))
		# future = asyncio.ensure_future(get_url(url))
		# tasks.append(future)

	for task in asyncio.as_completed(tasks):
		result = await task
		print(result)


if __name__ == '__main__':
	start_time = time.time()
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
	print('last time {}'.format(time.time()-start_time))
"""
